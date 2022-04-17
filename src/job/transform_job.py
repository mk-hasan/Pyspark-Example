"""
Author: Kamrul Hasan
Date: 16.04.2022
Email: hasan.alive@gmail.com
"""

from pyspark.sql.types import StringType, StructField, StructType, TimestampType
import pandas as pd


class TranformJob:
    """
    A Calss to to run all the transformation jobs
    """
    def __init__(self, spark_session, helper_utils, config) -> None:
        """
        The default constructor
        :param spark_session: Spark Session
        :param helper_utils: Utils Class
        :param config: Config data
        """
        self.source_path = config['input_path']
        self.spark_session = spark_session
        self.helper_utils = helper_utils
        self.logger = TranformJob.__logger(spark_session)

    def run(self) -> None:
        """
        Main transform class to run all jobs and save the data into absolute sink location
        """
        self.logger.info('Running Transformation Job')

        df_schema = StructType(
            [
                StructField('time', TimestampType()),
                StructField('action', StringType())
            ]
        )
        # read the input file
        data_frame = self.spark_session.read.csv(self.source_path, header=True, schema=df_schema)
        data_frame_by_minute = self.helper_utils.to_minute(data_frame)

        # get the different action type and the total count
        dataframe_by_action_type = self.helper_utils.count_action_type(data_frame_by_minute)
        dataframe_by_action_type.toPandas().to_csv("../../resources/data/result/df_action_type.csv")

        # get the average number of action by per 10 minute
        dataframe_avg_action_no = self.helper_utils.avg_no_action(data_frame_by_minute)
        dataframe_avg_action_no.toPandas().to_csv("../../resources/data/result/df_avg_no_action.csv")

        # get the biggest number of action by the time frame
        data_frame_biggest_tf = self.helper_utils.get_biggest_time_frame(data_frame_by_minute)
        pd.DataFrame(list(data_frame_biggest_tf)).to_csv("../../resources/data/result/df_biggest_time_frame.csv")

        self.logger.info('End running TransformationJob')

    @staticmethod
    def __logger(spark_session) :
        """
        Logger method to get the logging
        :param spark_session: Spark Session
        :return: Logmanager instance
        """
        log4j_logger = spark_session.sparkContext._jvm.org.apache.log4j  # pylint: disable=W0212
        return log4j_logger.LogManager.getLogger(__name__)

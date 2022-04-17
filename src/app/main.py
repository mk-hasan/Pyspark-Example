"""
Author: Kamrul Hasan
Date: 16.04.2022
Email: hasan.alive@gmail.com
"""

from pyspark.sql import SparkSession

from src.job.transform_job import TranformJob
from src.utils.utils import HelperUtils


def run() -> None:
    """
    A simple function to create the spark session and triggers the jobs.
    """
    spark_session = SparkSession \
        .builder \
        .appName('lidl-app') \
        .getOrCreate()

    helpers_utils = HelperUtils()
    config = helpers_utils.config_loader()
    TranformJob(spark_session, HelperUtils, config).run()


if __name__ == '__main__':
    run()

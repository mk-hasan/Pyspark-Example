"""
Author: Kamrul Hasan
Date: 16.04.2022
Email: hasan.alive@gmail.com
"""


import json
from pathlib import Path
from pyspark.sql.functions import col, window, hour, minute, second, collect_set, explode, date_trunc
from pyspark.sql import functions as F


class HelperUtils:

    @staticmethod
    def to_minute(df):
        """
        A function to take the timesatmp with minute, truncate seconds
        :param df: Spark Dataframe
        :return: Spark Dataframe
        """
        return df.withColumn("time", date_trunc("minute", col("time")))

    @staticmethod
    def count_action_type(df_minute) :
        """
        A function to groupby and count total action
        :param df_minute: Spark Dataframe
        :return: Spark Dataframe
        """
        cnt_cond = lambda cond: F.sum(F.when(cond, 1).otherwise(0))
        df_open_close_count = df_minute.groupBy('time').agg(
            cnt_cond(F.col('action') == 'Open').alias('open_cnt'),
            cnt_cond(F.col('action') == 'Close').alias('c_cnt')).orderBy('time')
        return df_open_close_count

    @staticmethod
    def avg_no_action(df):
        """
        A function to groupby and product avg number of action each 10 minute
        :param df: Spark Dataframe
        :return: Spark Dataframe
        """
        df_minute_count = df.groupBy('time').count().orderBy('time')
        df_10_minute_count = transform_to_minute_interval(df_minute_count)
        df_final = df_10_minute_count.groupBy("window10").agg(F.mean('count'))
        return df_final

    @staticmethod
    def get_biggest_time_frame(df):
        """
        A function to groupby and count total action
        :param df: Spark Dataframe
        :return: set object
        """
        cnt_cond = lambda cond: F.sum(F.when(cond, 1).otherwise(0))
        df_10_minute = transform_to_minute_interval(df)
        df_bigger_amount_open = df_10_minute.groupBy('window10').agg(
            cnt_cond(F.col('action') == 'Open').alias('open_cnt')).orderBy('open_cnt', ascending=False)
        return {df_bigger_amount_open.collect()[0][0], df_bigger_amount_open.collect()[0][1]}

    @staticmethod
    def config_loader():
        """
        A function to load config file
        :return: json object
        """
        try:
            with open("../../resources/config/config.json", 'r') as f:
                config = json.load(f)
        except IOError:
            print("Error: File does not appear to exist.")
            return 0
        return config


def transform_to_minute_interval(df):
    """
    A function to convert the dataframe to 10 minute window ,
     the starting offset is 5 of each ten minute but it can be dynamically change based on the first row(min timestamp)
    :param df_minute: Spark Dataframe
    :return: Spark Dataframe
    """
    df_10_minute = df.withColumn(
        "window10",
        window(
            col("time").cast("string"),
            windowDuration="10 minute", slideDuration="10 minute", startTime='5 minutes'
        )
    )
    return df_10_minute

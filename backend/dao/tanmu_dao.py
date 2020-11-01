from typing import List

from models.tanmu import Tanmu
from utils.db_utils import Select, Insert


class TanmuDao:
    @classmethod
    @Select("select * from mac_tanmu where vod_id = %(vod_id)s and play_url = %(play_url)s order by `current_time_int`")
    async def get_by_vod_id_and_play_url(cls, vod_id: int, play_url: str) -> List[Tanmu]:
        pass

    @classmethod
    @Insert("insert into mac_tanmu "
            " (`vod_id`, `play_url`,`content`, `current_time`, `current_time_int`, `user_id`, `create_time`) "
            " VALUES (%(vod_id)s, %(play_url)s, %(content)s, %(current_time)s,"
            " %(current_time_int)s, %(user_id)s, %(create_time)s)")
    async def insert_danmu(cls, vod_id, play_url, content, current_time, current_time_int, user_id, create_time):
        pass

    # @classmethod
    # @Select("""\
    # SELECT `current_time_int`,
    #    CONCAT('[',
    #           GROUP_CONCAT(
    #                   JSON_OBJECT(
    #                           'content', content,
    #                           'vod_id', vod_id,
    #                           'current_time' , `current_time`,
    #                           'styles' , `styles`
    #                       ) order by `current_time` asc
    #               ), ']'
    #        ) AS list
    #     FROM mac_tanmu
    #     WHERE vod_id =  %(vod_id)s GROUP BY `current_time_int`
    # """)
    # async def get_by_vod_id_and_group_by_time(cls, vod_id):
    #     pass
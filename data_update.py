
from my_parser import my_parser
from analytics import create_analytics_content


async def data_update():
    # обновление данных
    my_parser.england_parser()
    my_parser.german_parser()
    my_parser.italy_parser()
    my_parser.statistics_parser()
    my_parser.spain_parser()
    my_parser.france_parser()
    my_parser.club_statistics_parser()



async def analytics_update():
    # обновление данных
    create_analytics_content.analytics_content_country()
    create_analytics_content.analytics_content_club()



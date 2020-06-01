import logging
import os

from binance_api import Binance

bot = Binance(
    API_KEY='DdL1WpiHMChk4DWgrdirKTYAWkeWxVUvtyCGWRSdhGhqWi5Gtcze6Bv4s0dFCKVW',
    API_SECRET='WxvPEgYNvxWPSJQuvvqIySSkamsMdRL3QroD3mQukIz9gr2sAzMQaAMa26ANNZBL'
)

"""
    Пропишите пары, на которые будет идти торговля.
    base - это базовая пара (BTC, ETH,  BNB, USDT) - то, что на бинансе пишется в табличке сверху
    quote - это квотируемая валюта. Например, для торгов по паре NEO/USDT базовая валюта USDT, NEO - квотируемая
"""
pairs = [
   {
        'base': 'BNB',
        'quote': 'ZEC',
        'spend_sum': 0.0011,  # Сколько тратить base каждый раз при покупке quote
        'profit_markup': 0.5, # Какой навар нужен с каждой сделки? (1=1%)
        'use_stop_loss': False, # Нужно ли продавать с убытком при падении цены
        'stop_loss': 1, # 1% - На сколько должна упасть цена, что бы продавать с убытком
        'active': True,
    }
]

KLINES_LIMITS = 500
POINTS_TO_ENTER = 7


"""
    USE_OPEN_CANDLES = True - использовать последнюю (текущую) свечу для расчетов
    USE_OPEN_CANDLES = False - Использовать только закрытые свечи

    Например, если USE_OPEN_CANDLES = False и таймфрейм часовой, и время 13:21, то будут браться свечи до 13:00.
    После 14:00 свеча с 13:00 по 14:00 тоже попадет в выборку, но не будет браться 14:00 - 15:00 и т.п.
"""
USE_OPEN_CANDLES = True 

TIMEFRAME = "1h"
'''
    Допустимые интервалы:
    •    1m     // 1 минута
    •    3m     // 3 минуты
    •    5m    // 5 минут
    •    15m  // 15 минут
    •    30m    // 30 минут
    •    1h    // 1 час
    •    2h    // 2 часа
    •    4h    // 4 часа
    •    6h    // 6 часов
    •    8h    // 8 часов
    •    12h    // 12 часов
    •    1d    // 1 день
    •    3d    // 3 дня
    •    1w    // 1 неделя
    •    1M    // 1 месяц
'''




# Подключаем логирование
logging.basicConfig(
    format="%(asctime)s [%(levelname)-5.5s] %(message)s",
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler("{path}/logs/{fname}.log".format(path=os.path.dirname(os.path.abspath(__file__)), fname="binance")),
        logging.StreamHandler()
    ])
log = logging.getLogger('')


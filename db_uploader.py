import random
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starbugs.settings")
django.setup()

from product.models import *
from user.models import *

from django.db import transaction


@transaction.atomic
def transaction():

    DRINK_STATUS = ["강달쌘","강달약","강짭쌘","강짭약","부달쌘","부달약","부짭쌘","부짭약"]

    DrinkStatus.objects.get_or_create(id=1, name = "강달쌘")
    DrinkStatus.objects.get_or_create(id=2, name = "강달약")
    DrinkStatus.objects.get_or_create(id=3, name = "강짭쌘")
    DrinkStatus.objects.get_or_create(id=4, name = "강짭약")
    DrinkStatus.objects.get_or_create(id=5, name = "부달쌘")
    DrinkStatus.objects.get_or_create(id=6, name = "부달약")
    DrinkStatus.objects.get_or_create(id=7, name = "부짭쌘")
    DrinkStatus.objects.get_or_create(id=8, name = "부짭약") 

    # 카테고리
    main_category = MainCategory.objects.create(name="음료")
    # 서브카테고리
    SUBCATEGORIES = [
        ("콜드브루", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("브루드 커피", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("에스프레소", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("프라푸치노", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("블렌디드", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("스타버스 파지오", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("티(티바나)", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("기타 제조 음료", "디카페인 에소프레소 삿 츄가가능(일부음료제외)"),
        ("스타벅스 주스(병음료)", "111")
    ]
    for subcategory in SUBCATEGORIES:
        SubCategory.objects.get_or_create(
            name=subcategory[0],
            description=subcategory[1],
            main_category=main_category
        )


    coldbrew       = SubCategory.objects.get(name="콜드브루")
    broodcoffee    = SubCategory.objects.get(name="브루드 커피")
    espresso       = SubCategory.objects.get(name="에스프레소")
    frappuccino    = SubCategory.objects.get(name="프라푸치노")
    blended        = SubCategory.objects.get(name="블렌디드")
    pigio          = SubCategory.objects.get(name="스타버스 파지오")
    tea            = SubCategory.objects.get(name="티(티바나)")
    other_beverage = SubCategory.objects.get(name="기타 제조 음료")
    juice          = SubCategory.objects.get(name="스타벅스 주스(병음료)")

    # 음료
    
    DRINKS = [
        [coldbrew, "나이트로 바닐라 크림", "Nitro Vanilla Cream","부드러운 목넘김의 나이트로 커피와 바닐라 크림의 매력을 한번에 느껴보세요!","부드러운 목넘김의 나이로 커피와 바닐라의 매력을 느껴보세요!"],
        [coldbrew, "나이로 콜드 브루", "Nitro Cold Brew", "완벽한 밸런스에 커피 본연의 신맛을 경험할 수 있습니다.", "뜨거운 물로 25시간 동안 서서히 완성된 콜드 브루가 산소와 만나 부드러운 콜드 크레를 탄생시켰습니다. 부드러운 목넘김과 완벽한 밸런스에 커피 본연의 신맛을 경험할 수 있습니다. 격조 있는 커피가 어울리는 당신께 스타박스가 지금, 제안합니다."],
        [coldbrew, "돌체 콜드 브루", "Dolce Cold Brew", "무더운 여름철, 동남아 휴가지에서 즐기는 커피를 떠오르게 하는 스타벅스 ]음료의 콜드 브루를 만나보세요!","무더운 여름철, 동남아 휴가지에서 즐기는 커피를 떠오르게 하는 스타벅스 음료의 베스트조합인 돌체 콜드 브루를 만나보세요!"],
        [coldbrew, "바닐라 크림 브루", "Vanilla Cream Cold Brew", "콜드 브루에 더해진 바닐라 크림인음료입니다.","콜드 브루에 더해진 바닐라 크림인음료입니다."],
        [coldbrew, "비자림 콜드 브루", "Forest Cold Brew", "유기농 말차로 만든 파우더와 Cold Brew를 활용한 음료.", " 유기농 말차로 만든 파우더와 Cold Brew를 활용한 음료. 더욱 시원하고 새로운 Cold Brew를 즐겨보세요."],
        [coldbrew, "콜드 브루","Cold Brew", "스타 바리스타의 정성으로 탄생한 콜드 브루! ", "콜드 브루 전용 원두를 차가운 물로 14시간 동안 추출하여 신선하게 한정된 양만 제공됩니다. 부드럽고 그윽한 초콜릿 풍미의 콜드 브루를 만나보세요!"],
        [coldbrew, "콜드 브루 몽트","Cold Brew Malt", "바닐라 아이스크림, 몰트가 블렌딩된 리저브만의 쉐이크 ", "20시간 정성으로 추출한 리저브 콜드 브루와 미국산 프리미엄 바닐라 아이스크림 그리고 몰트를 블렌딩한 리저브만의 쉐이크 음료입니다."],
        [coldbrew, "콜드 브루 플르트","Cold Brew Float", "콜드 브루 위에 녹아 내리는 한 스쿱의 바닐라 아이스크림", "20시간 정성으로 추출한 콜드 브루에 뉴질랜드산 프리미엄 바닐라 아이스크림이 올려진 콜드 브루 음료입니다"],
        [broodcoffee, "아이스 커피","Iced Coffee",  "깔끔하고 상큼함이 특징인 시원한 아이스 커피", "케냐, 하우스 블렌드 등 약간의 산미가 있는 커피를 드립 방식으로 추출한 후 얼음과 함께 제공하는 커피 입니다"],
        [broodcoffee, "내일의 커피", "Brewed Coffee","신선하게 브루드(Brewed)되어 원두의 다양함이 살아있는 커피","매주 일주일 간격으로 하나의 원두 종류를 선정하여 신선하게 브루드(Brewed)되어 제공되는 드립커피로 원두 커피의 풍부한 맛과 향을 따뜻하게 즐기실 수 있습니다."],
        [espresso, "에스프레소 코피나", "Espresso Con Panna", "에스프레소 샷에 풍부한 휘핑크림을 얹은 강렬하고 달콤한 음료", "신선한 에스프레소 샷에 풍부한 휘핑크림을 얹은 커피 음료로서, 뜨거운 커피의 맛과 차갑고 달콤한 생크림의 맛을 동시에 즐기실 수 있습니다."],
        [espresso, "에스프레소 마키아또", "Espresso Macchia", "강렬한 에스프레소 위에 대량의 우유 거품이 얹어진 음료","신선한 에스프레소 샷에 우유 거품을 살짝 얹은 커피 음료로써, 강렬한 에스프레소의 맛과 우유의 거침을 같이 느끼실 수 있습니다."],
        [espresso, "아이스 아메리카노", "Iced Caffe Americano", "강렬한 에스프레소 샷에 시원한 불의 조화", "연한 농도의 에스프레소에 시원한 정수물을 더하여 스타벅스의 깔끔하고 강렬한 에스프레소를 부드럽지만 시원하게 즐기실 수 있는 커피입니다."],
        [espresso, "카페 아메리카노", "Caffe America", "강렬한 에스프레소 샷에 뜨거운 불의 조화", "유럽풍의 커피를 미국 스타일로 접목시킨 커피로써, 연한 농도의 에스프레소와 더운물을 혼합하여, 스타벅스의 깔끔하고 강렬한 에스프레소를 가장 거침을 잘 느낄 수 있는 커피입니다."],
        [espresso, "아이스 까라메 마끼아또", "Iced Caramel Macchiato", "바닐라 시럽, 시원한 우유에 얼음과 에스프레소 샷, 까라메 드리즐이 어우러진 음료", "향긋한 바닐라 시업과 뜨거운 우유에 얼음을 넣고 점을 찍듯이 에스프레소를 부은 후 다리모양으로 카라멜 소스를 뿌려 장식한 음료로 가장 아름다운 커피 음료 중 하나입니다."],
        [espresso, "끼라메 마키아또", "Caramel Macchiato", "바닐라와 우유, 그리고 그 위에 얹어진 에스프레소 샷과 달콤한 끼라메 드리즐의 조화", "향긋한 바닐라 시럽과 차가운 스팀밀크 위에 풍성한 우유 거품을 얹고 점을 찍듯이 에스프레소를 부은 후 다리모양으로 카라멜 소스를 뿌려 장식한 달콤한 커피 음료입니다."],
        [espresso, "아이스 코푸나여", "Iced Cappuccino", "에스프레소 샷과 시원한 우유에 부드러운 우유 거품이 시원한 음료.", "부실하고 연한 농도의 에스프레소에 시원한 우유를 더하여 우유의 고소함과 에스프레소의 강렬함에 벨벳같은 물이 더해져 부드러운 커피 입니다."],
        [espresso, "코푸나여", "Cappuccino", "레드벨벳같은 물과 에스프레소 샷의 절묘한 조화!", "풍부하고 진한 농도의 에스프레소에 따뜻한 물과 레드벨벳같은 우유 거품이 2:1 비율로 어우러저 마무리된 대표적인 에스프레소 음료 입니다."],
        [frappuccino, "원 에스프레소 찹 프라푸치노","One Espresso Chip Frappuccino", "에스프레소 2샷과 에스프레소 칩, 하프앤하프가 곁들여진 커피", "리스트레토 에스프레소 2샷과 에스프레소 칩, 하프하프가 달고 연하게 어우러진 커피의 기본에 충실한 더블 에스프레소 찹 프라푸치노를 만나보세요."],
        [frappuccino, "무카 프라푸치노","Mocha Frappuccino", "초콜릿, 커피와 얼음이 갈린 음료에 휘핑크림이 토핑된 음료입니다.", "'너만의 프라푸치노'로 변경되어 물 선택과 커피 농도 조절이 가능한 블렌디드 음료입니다."],
        [frappuccino, "에소프레소 프라푸치노", "Espresso Frappuccino", "에스프레소의 열렬함과 약간의 신맛을 시원하게 즐기는 프라푸치노입니다.", "분쇄된 얼음과 뜨거운 커피에 풍부하고 진한 에스프레소 삿이 더해진 음료입니다."],
        [frappuccino, "지바 찹 프라푸치노", "Jiva Chap Frappuccino", "커피 프라푸치노에 초콜릿, 초콜릿 찹이 첨가된 블렌드로 달콤 아삭한 음료입니다.", "초콜릿 시럽 그리고 연한 초콜릿 칩이 입안에 느껴지는 스타벅스에서만 맛보실 수 있는 개념 음료로 시원한 커피와 함께 초콜릿 칩의 쌉히는 맛이 이색적입니다."],
        [frappuccino, "키라메 프라푸치노", "Caramel Frappuccino", "시럽이 더해진 커피 프라푸치노에 크림, 키라멜이 장식된 음료입니다.", "시원한 커피와 시럽이 조화를 이루며 그위에 크림을 얹고 달콤한 키라메로 장식한 커피 음료로, 스타벅스에서 가을에 가장 인기있는 음료입니다."],
        [frappuccino, "화이트 초코릿 무카 프라푸치노", "White Chocolate Mocha Frappuccino", "화이트 초콜릿, 커피와 우유가 조합된 아이스 블렌드로 휘핑크림이 토핑된 음료입니다.", "뜨거운 커피와 화이트 초콜릿 시럽, 휘핑크림이 조화를 이루며 코코아 파우더로 마무리한 음료입니다."],
        [frappuccino, "바닐라 프라푸치노", "Cream Frappuccino", "물에 바닐라향이 조합된 블렌드로 휘핑이 토핑된 음료입니다.", "신선한 우유와 크림 프라푸치노 풍미에 시럽이 조화를 이루며 그 위에 휘핑으로 마무리된 음료입니다."],
        [frappuccino, "초콜릿 찹 프라푸치노", "Cream Chip Frappuccino", "모카시럽과 지바칩이 혼합된 크림 프라푸치노로 휘핑크림 음료입니다.", "신선한 우유와 크림 프라푸치노 풍미에 달콤한 초콜릿 시럽과 초콜릿 칩이 더해져 아싹아싹 씹히는 맛이 특징적인 음료입니다."],
        [blended, "딸기 젤리 블렌디드","Strawberry Jelly Blended", "딸기의 요즘 트렌드는 말랑말랑 딸기 찹쌀 떡!", "상큼&말랑&부드러운 딸기의 식감으로 딸기의 새로운 조합!"],
        [blended, "망고 푸르츠 블렌디드", " Fruit Blended", "연한 블랙 티에  패션 푸르츠 주스가 조합된 아이스 블렌드 음료", "달콤한 망고 패션 푸르츠 주스에 연하게 추출된 블랙 티를 얼음과 함께 블렌드한 음료로 깔끔하고 뜨거움이 특징적인 음료입니다."],
        [blended, "딸기 유거트 블렌디드", "Yogurt Blended", "요거트의 상큼함이 가득 느껴지는 무거운 컨셉의 블렌디드 음료입니다.", "요거트와 유지방 우유, 딸기가 어우러져 가볍고 시큼하게 즐길 수 있는 블렌디드 음료입니다. 식감과 풍미가 부실하게 느껴지는 딸기를 요거트와 함께 음료로 즐겨보세요!"],
        [blended, "망고 바나나 블렌다드", "Mango Bana Blended", "인기 음료인 망고 패션후르츠 블렌디드에  바나나 2개가 통째로 들어간 시큼한 프라푸치노", " 음료 한잔으로 무거운 맛 뿐만 아니라 부지런함까지 얻을 수 있는 망고 바나나 블렌디드를 추천합니다."],
        [blended, "자몽 숏 블렌디드", "Grapefrui Blended", "시큼한 레모네이드가 얼음과 가볍고 시원하게 즐길 수 있는 블렌디드 음료.", "시큼함으로 끝까지 시원한 자몽 셔벗 블렌디드!"],
        [blended, "피&레 블렌디드", "Pea & Le Blended", "딱딱한 복숭아 청량한 피치 & 레몬 블렌디드로 올 겨울을 맞이해보세요.", "딱딱한 복숭아 젤리가 만난 맑고 청량한 피치 & 레몬 블렌디드로 겨울을 맞이해보세요"],
        [pigio, "하얀 티 레몬 피지오", "White Tea Lemonade Fazzio", "하얀 티와 시큼한 레모네이드를 스파쿨링한 시원하고 청량감 있는 음료입니다.", "연하게 우린 하얀 티와 상큼한 레모네이드를 더한 뒤,  나만의 전용 머신을 이용해 스파클링한, 청량감 있는 음료입니다."],
        [pigio, "풀 타입 파지오", "Full Lime Starbucks Fazzio", "반건조된 라임 슬라이스를 넣고 스파클링한 시원하고 행복한 음료입니다. ", "톡톡 튀는 수제 스파클링과 톡 쏘는 풍미가 완벽하게 어우러진 풀 타입 파지오와 함께 오늘 하루도 가볍고 힘차게 시작해 보세요!"],
        [pigio, "패션 레모네이드 파지오", "Tea Lemonade Fazzio", "상큼한 레모네이드를 스파클링한 시원하고 청량감 있는 음료입니다.", "언제 찾아도 기분이 좋아지는 훌륭한 음료입니다."],
        [pigio, "자몽 파지오", "Pink Grapefruit Fazzio", "핑크빛의 생자몽으로 비주얼과 신선함을 느끼자.", "신선한자몽이 수제 탄산음료입니다."],
        [tea, "딸기 티", "Shaken Tea", "깔끔하게 즐길 수 있는 어른이 맛의 음료.", "딸&라&레과 소량의 밀차 파우더로 상큼한 딸기 음료를 즐겨보세요."],
        [tea, "패션 티", "Fassion Tea", "국적인 조화가 매력적인 패션 티를 만나보세요!", "국적인 조화가 매력적인 라임 패션 티를 만나보세요!"],
        [tea, "만트 블렌디 티", "Mant Tea", "블렌딩된 상쾌한 허브 티 입니다.", "타라곤을 곁들인 맑은 풋풋함이 특징인 티 음료 입니다"],
        [tea, "라이 패션 티", "Lie Tea", "국적인 조화가 매력적인 라임 패션 티를 만나보세요!", "국적인 조화가 매력적인 라임 패션 티를 만나보세요!"],
        [tea, "아이스 만트 티", "Ice Mant Tea", "레몬이 블렌딩된 상쾌한 허브 티 입니다.", "시원한 풋풋한 허브 티로 페퍼민트와 스피어민트에 따뜻한 파라콘을 곁들인 맑은 상쾌함이 특징인 티 음료 입니다."],
        [tea, "아이스 알 그레 티", "Ice Earl Gre Tea", "라벤더 향이 특징적인 향긋한 티", "조화를 이루면서 부드럽고 깊은 풍미가 특징인 티 음료 입니다."],
        [tea, "아이스 유스 티", "Iced Youth Tea", " 베리류의 새콤함을 느낄 수 있는 티 입니다.", "화이트 티로 선홍빛의 허브 티 입니다."],
        [tea, "아이스 유자 만트 티", "Iced Yuja Mant Tea", "만트 티가 조화로운 유자 민트 티입니다.", "상쾌한 민트 티가 조화로운 유자 만트 티입니다."],
        [other_beverage, "딸기 라떼", "Strawberry Latte", "딸기 베이스로 시큼하게 신선한 딸기 음료를 즐기자.", "갓 수확한 딸기 베이스로 시큼하게 딸기 음료를 즐기자"],
        [other_beverage, "핫 초코릿", "hot chocolate", "휘핑크림과 코코아 파우더가 얻어진 음료.", "크림을 얹고 코코아 파우더로 장식한 특별한 초콜릿 음료입니다."],
        [other_beverage, "아이스 초콜릿", "Iced Chocolate", "물에 휘핑과 파우더가 얹어진 음료.", " 크림과 파우더로 장식한 시원한 초콜릿 음료입니다."],
        [other_beverage, "판다 초콜릿", "Panda Chocolate", "귀여운 판다까지 더해진 판다 핫 초콜릿", "귀여운 판다까지 더해진 판다 핫 초콜릿"],
        [other_beverage, "스틸 우유", "Still Milk", "부드럽고 깨끗한 우유.", "우유를 스틸하여 거친 거품을 얹어 마무리한 차가운 우유입니다."],
        [other_beverage, "우유", "Milk", "고소하고 깨끗한 우유", "고소하고 깨끗한 우유"],
        [other_beverage, "까만 라뗴", "Black Latte", "고소하고 시큼한 토핑으로 어우러진 음료입니다.", "고소하고 시큼한 토핑으로 어우러진 음료입니다."],
        [other_beverage, "숙숙 라떼", "SukSuk Latte", "건강과 힐링을 느끼는 음료", "건강과 힐링을 통해 성장할 수 있는 최고의 음료"],
        [juice, "기운내라", "Lime and Lemon", "비타민C를 채워주는 주스", "비타민C를 채워주는 주스"],
        [juice, "파이팅하자", "Green Juice", "비타민C로 상큼해지는 주스.","비타민C로 상큼해지는 주스."],
        [juice, "이겨내자", "Orange Juice", "자연을 그대로 느낄 수 있는 주스.", "자연을 그대로 느낄 수 있는 주스."],
        [juice, "도와줘", "Black Juice", "곡물 음료로 비타민D까지 채우세요", "곡물 음료로 비타민D까지 채우세요"],
        [juice, "힘내자", "Straw Juice", "외국산 딸기가 듬뿍 느껴지는 주스", "외국산 딸기가 듬뿍 느껴지는 주스"],
        [juice, "사랑해", "Mango Juice", "망고가 정말 느껴지는 주스", "망고가 정말 느껴지는 주스"],
        [juice, "해보자", "Water Juice", "수박의 달달함이 느껴지는 주스", "수박의 달달함이 느껴지는 주스"],
        [juice, "행복하자", "Apple Juice", "과일에 달콤함이 느껴지는 주스", "과일에 달콤함이 느껴지는 주스"],
    ]

    IMAGE_URL = [
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/andrew-donovan-valdivia-Bb-8qt2tFDs-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/ash-edmonds-mzoivEr2G2w-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/billy-kwok-vfiA7rRtjWo-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/food-photographer-jennifer-pallian-sSnCZlEWN5E-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/jenny-pace-K5IUb0kBZZ8-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/kayra-sercan-oNqRZ7XKJHQ-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/mazniha-mohd-ali-noh-4mqYiircf7s-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/melissa-walker-horn-gtDYwUIr9Vg-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/sandra-seitamaa-akwA-GPF710-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/shenggeng-lin-XoN3v3Ge7EE-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/waldemar-brandt-RyxiuEv6ssk-unsplash.jpg",
       "https://jinukix-bucket.s3.ap-northeast-2.amazonaws.com/william-moreland-eSzClaMXNkk-unsplash.jpg"
    ]

    for i in DRINKS:
        
        x = 1

        feel = random.randint(0,100)
        if feel >= 50:
            x +=4 

        taste = random.randint(0,100)
        if taste >= 50:
            x += 2

        destiny = random.randint(0,100)
        if destiny >= 50:
            x += 1

        Drink.objects.get_or_create(
            sub_category=i[0],
            korean_name=i[1],
            english_name=i[2],
            main_description=i[3],
            sub_description=i[4],
            is_new = random.choice([True, False]),
            is_season= random.choice([True, False]),
            price = random.choice([3000, 3500, 4000, 4500, 5000, 5500, 6000]),
            image_url = random.choice(IMAGE_URL),
            destiny = destiny,
            taste = taste,
            feel = feel,
            drink_status = DrinkStatus.objects.get(id=x)
        )

    # 알레르기
    ALLERGY = ["우유", "대두","밀", "토마토", "복숭아"]
    for i in ALLERGY:
        Allergy.objects.get_or_create(name=i)

    # drink allergy
    number = [1,2,3]
    for i in Drink.objects.all():
        random.shuffle(number)
        for j in range(number[0]):
            allergy = Allergy.objects.get(name=random.choice(ALLERGY))
            DrinkAllergy.objects.get_or_create(drink = i, allergy=allergy)

    # Size
    for i in ["Tall(톨)", "Grande(그란데)"]:
        Size.objects.create(name = i)
    
    # 영양 정보
    for i in Drink.objects.all():
        kcal       = random.randint(1,20)
        sodium     = random.randint(1,20)
        saturation = random.randint(1,20) 
        sugar      = random.randint(1,20) 
        protein    = random.randint(1,20) 
        caffeine   = random.randint(1,20)
        Nutrition.objects.get_or_create(
                                        drink      = i,
                                        size       = Size.objects.get(name = "Tall(톨)"),
                                        kcal       = kcal,
                                        sodium     = sodium,
                                        saturation = saturation,
                                        sugar      = sugar,
                                        protein    = protein,
                                        caffeine   = caffeine
        )
        
        Nutrition.objects.get_or_create(
                                        drink      = i,
                                        size       = Size.objects.get(name = "Grande(그란데)"),
                                        kcal       = kcal * 2, 
                                        sodium     = sodium * 2, 
                                        saturation = saturation * 2, 
                                        sugar      = sugar * 2, 
                                        protein    = protein * 2, 
                                        caffeine   = caffeine * 2 
        )



transaction()


import streamlit as st
import pandas as pd
import random

# 페이지 설정
st.set_page_config(
    page_title="MBTI 티니핑 추천 💖",
    page_icon="🌸",
    layout="centered"
)

# MBTI별 티니핑 데이터 (16개 모두 다름!)
tinyping_data = {
    "INTJ": {
        "name": "차차핑",
        "emoji": "🧊❄️",
        "image": "https://i.namu.wiki/i/cg2RlnSasAgScmXMvQw94dNOOCXozN1xMo5ppewr2a8jsbltWBGL3kB8ygCAwuuZyGIojS9Bq1OwBMBYvQInOXexcNX0bju4x6J-VLwLTxWZx1XVDOrvHEK_4OyS7PNqAZI3M4LQdShNLhB-KBdjTg.webp",
        "description": "차갑고 시크하지만 속은 깊은 매력! 자기 세계가 확실한 너에게 딱이야~",
        "personality": "냉철한 전략가",
        "fact": "❄️ 차가운 마음의 티니핑! 시크함 뒤에 숨겨진 진심이 매력이야~",
        "quote": "흥, 별로 관심 없거든?",
        "color": "#4A90E2",
        "bg_color": "#E3F2FD"
    },
    "INTP": {
        "name": "아잉핑",
        "emoji": "🤔💭",
        "image": "https://i.namu.wiki/i/l2PVq5UTMpHHVTuqu4Z7le8jn62Q_TF3pJGRY7MOoDwmJV69bN_IBRQv0jxT5sBV-9cmJAWoSwB0wBu8YC5bQHXJ1xD_Ygg03isvLnwUQD9LmHVoDI17w9am_SJTuPX7cIVOFyY3ITFN2LiTr6c3Rg.webp",
        "description": "엉뚱하고 호기심 가득한 너! 알쏭달쏭 아잉핑과 환상의 콤비~",
        "personality": "엉뚱한 호기심쟁이",
        "fact": "💭 '아잉~' 하면서 헷갈리게 만드는 매력의 소유자!",
        "quote": "아잉~ 이게 뭐지?",
        "color": "#9B59B6",
        "bg_color": "#F3E5F5"
    },
    "ENTJ": {
    "name": "나르핑",
    "emoji": "👑💎",
    "image": "https://i.namu.wiki/i/k0HJvM1xxQ2giqQ60O23Hb674pOTL0AmIvrjuTocW-LJlXOb3iQ3MFzqSqtZbQZq5hQIGCjK6ElThCXZ6NOXbBP7rGJ7R8-sZ_hR1EqRcbE6mh-8OIRPc5C3WIHzlg2vtY1-PsRZv7Lw74h8bX5rMQ.webp",  # 직접 이미지 추가하기!
    "description": "당당하고 카리스마 넘치는 리더! 자존감 만렙 나르핑과 너무 잘 어울려~",
    "personality": "도도한 카리스마 여왕",
    "fact": "👑 자기애 충만! 당당함의 끝판왕 공주 티니핑~",
    "quote": "내가 제일 잘나가~!",
    "color": "#E74C3C",
    "bg_color": "#FFEBEE"
},
    "ENTP": {
        "name": "악동핑",
        "emoji": "😈✨",
        "image": "https://i.namu.wiki/i/9Fne-VPqsl5BA5SV-LnFA3NHozjN5sHTxQYDHGpD6HAsGQu2_XR4Rn_fESjPYNqjIOntP-clYtk0b_w7oYyPEDNw_wvFxVnmRqa-X2KA-jyhniQRaLnwkpsPRQcVMoby5m8mR6BdjMXeYyJzwEaKlA.webp",
        "description": "장난기 가득! 아이디어 뱅크인 너와 악동핑은 환상의 짝꿍!",
        "personality": "재치만점 트러블메이커",
        "fact": "😈 장난치는 걸 제일 좋아하는 악동! 하지만 미워할 수 없어~",
        "quote": "히히! 장난쳐볼까?",
        "color": "#F39C12",
        "bg_color": "#FFF3E0"
    },
    "INFJ": {
        "name": "하츄핑",
        "emoji": "💗🌷",
        "image": "https://i.namu.wiki/i/Yq5c-LYU0RjCDFk5y025VS3LJTtTujWhCIb_nS89AaeOf-60v9_0PE5p13POFRrGjrOv9H0iMdMilwYyCO6cSkP8i9w1YHA5eokCQruwk-nx0v4rfw60xkP0Qi9r2f-91hANUnuQtI4tAs6IOHkpyQ.webp",
        "description": "따뜻하고 사랑이 넘치는 너! 사랑의 요정 하츄핑과 영혼의 단짝!",
        "personality": "사랑둥이 힐러",
        "fact": "💗 사랑의 마음을 전해주는 메인 티니핑! 모두를 행복하게 해~",
        "quote": "사랑의 하츄핑이 나가신다~!",
        "color": "#FF69B4",
        "bg_color": "#FCE4EC"
    },
    "INFP": {
        "name": "라라핑",
        "emoji": "🎵💜",
        "image": "https://i.namu.wiki/i/nv2lQ5M6VvxvOcdpW9ZumWLmzlTZjw6UFdi-CWmHEDfZohhHthPKdQnD8aasngUaPtokoXN37CK9ZKxV7TNrCuWkhlkToFe8ASUO4Lh7Bopbo8tnmGMycDdzT9Kut2pggQHjILld9-_6WFNqRgBygg.webp",
        "description": "감수성 풍부한 예술가 타입! 음악을 사랑하는 라라핑과 찰떡이야~",
        "personality": "감성충만 아티스트",
        "fact": "🎵 노래와 음악을 사랑하는 티니핑! 감성 폭발 매력~",
        "quote": "라라라~ 노래 부르자!",
        "color": "#B19CD9",
        "bg_color": "#F3E5F5"
    },
    "ENFJ": {
        "name": "해핑",
        "emoji": "☀️😊",
        "image": "https://i.namu.wiki/i/a3uoGQU_VXpIEmE1wFrA7Vfco8zevlGZLU3jkGTEdlWZHhz_1rEXzgl3XB7p_B9h8hwY-7wGj2tbFG4JR06O88hAl2VzFL9RlefoA1kGUP0C-_-a8_WWNcYo9OflZSwJjmItTrtF6rZGklW6OMwYSQ.webp",
        "description": "밝고 따뜻한 너의 에너지! 햇살 같은 해핑과 너무 잘 어울려~",
        "personality": "햇살같은 행복전도사",
        "fact": "☀️ 햇살처럼 따뜻하게 모두를 비춰주는 천사 티니핑~",
        "quote": "오늘도 행복한 하루야!",
        "color": "#FFD700",
        "bg_color": "#FFFDE7"
    },
    "ENFP": {
        "name": "바로핑",
        "emoji": "🌈🎉",
        "image": "https://i.namu.wiki/i/IFpi2gWDo6WYv4iaeIMLFEWjQQEpcX4ytaY8YgRIkq1nxvHcBrMUik56uHuYvhKVIhe6JyXugTSjZIpVvi1Vs-B72n5lHa-Bg8qnBlr2ZXIC5vcLAKVzr20YDjGJT3aI5pHPvIhznBaV2-LGPQNOJA.webp",
        "description": "에너지 폭발 자유로운 영혼! 변신의 달인 바로핑과 환상의 콤비!",
        "personality": "자유로운 변신요정",
        "fact": "🌈 '바로 바로!' 다양하게 변신하는 만능 티니핑~",
        "quote": "바로바로 변신!",
        "color": "#FF6B9D",
        "bg_color": "#FCE4EC"
    },
    "ISTJ": {
        "name": "꾸래핑",
        "emoji": "📚🎀",
        "image": "https://i.namu.wiki/i/fwI1dwKAUK2c8_imisazbTjMEP8osoE2naMv-5m4pyVmUe6KnzgzLr3XxGa6424UyKkFOGofQmfTFOrTgfzB49zwtzZ7s4ylVw2cEiH-pfZaJXTp1Vs_RlW6PXTlj2T3rEwwt6179x8_bYp-mwOvOw.webp",
        "description": "성실하고 책임감 강한 너! 꼼꼼한 꾸래핑과 환상의 짝꿍이야~",
        "personality": "성실한 모범생",
        "fact": "📚 매일 꾸준히 무언가를 하는 성실 끝판왕 티니핑!",
        "quote": "꾸준히 하면 다 돼!",
        "color": "#8B7355",
        "bg_color": "#EFEBE9"
    },
    "ISFJ": {
        "name": "포실핑",
        "emoji": "🧸💕",
        "image": "https://i.namu.wiki/i/vaVb2aK0O3eDQvNaKY64fg9ZVKCSw9oSj0Ov3yRzLqs3i3MaDzTvFXAqjNhjO2BHa6QIS5LOqCUhFrd5EVt7j6hqpBFxcCdlymtupyMajTL4DPQDcmwFWGeL67QdcojvTqmAj4akiDckb8x9UxGofA.webp",
        "description": "포근하고 다정한 너! 따뜻한 마음의 포실핑과 닮은 매력이야~",
        "personality": "포근한 힐링요정",
        "fact": "🧸 포근포근한 마음으로 친구들을 챙겨주는 다정한 티니핑~",
        "quote": "포실포실~ 안아줄게!",
        "color": "#FFB6C1",
        "bg_color": "#FCE4EC"
    },
    "ESTJ": {
        "name": "똑똑핑",
        "emoji": "🎓📖",
        "image": "https://i.namu.wiki/i/RsKQXVgWZJBqMqgVTYBxJ8oqHJ-yCKvN2VYwzlqGZQNvCsZsR8x_z9F2QqM0PqJ3PqQ7Hl_NhFvqVOlJ1L_NPg.webp",
        "description": "체계적이고 야무진 너! 똑똑한 친구 똑똑핑과 너무 잘 어울려~",
        "personality": "야무진 우등생",
        "fact": "🎓 모르는 게 없는 척척박사 티니핑! 똑소리 나는 매력~",
        "quote": "그건 내가 알지!",
        "color": "#27AE60",
        "bg_color": "#E8F5E9"
    },
    "ESFJ": {
        "name": "정의핑",
        "emoji": "⚖️💖",
        "image": "https://i.namu.wiki/i/Pq3uVxEYmJ5XdF8vL1iZcQ_zXJlOPYJpxOeUzMNzGvxg-bAr5VnzKkLqXEZJEFOJfnP4DkN-mKvxLqJzS7tNYg.webp",
        "description": "정의롭고 사교적인 너! 모두를 챙기는 정의핑과 찰떡궁합!",
        "personality": "정의로운 히어로",
        "fact": "⚖️ 옳고 그름을 가리는 정의의 사도 티니핑! 든든해~",
        "quote": "정의는 반드시 승리해!",
        "color": "#FF4757",
        "bg_color": "#FFEBEE"
    },
    "ISTP": {
        "name": "샤샤핑",
        "emoji": "✂️🤍",
        "image": "https://i.namu.wiki/i/T4Bj7VgZW3XQK_LpVqYNRzMlOcEoP4nzKvFjGbXKYWLpAMQz5tNcRdVlJoXEbPqNzHk8DvJ3JmYxL1nNoSyKqg.webp",
        "description": "쿨하고 손재주 좋은 너! 시크한 매력의 샤샤핑과 닮았어~",
        "personality": "쿨한 만능 해결사",
        "fact": "✂️ 자기 일을 야무지게 해내는 쿨한 매력의 티니핑!",
        "quote": "샤샤샥~ 해결 완료!",
        "color": "#34495E",
        "bg_color": "#ECEFF1"
    },
    "ISFP": {
        "name": "딸기핑",
        "emoji": "🍓💝",
        "image": "https://i.namu.wiki/i/F7VEKtNz3R8XlCJZqNmYP_QwLPxJ-vYzGcK4nLMOEd9QpRT5sBvCxKYJzNqEPxJqLBfM4Q5CqOdJWXqNcVbKgw.webp",
        "description": "조용하지만 사랑스러운 너! 달콤한 딸기핑과 너무 잘 어울려~",
        "personality": "달콤상냥 매력쟁이",
        "fact": "🍓 딸기처럼 달콤하고 새콤한 매력의 티니핑~",
        "quote": "딸기처럼 달콤하게~",
        "color": "#FF1744",
        "bg_color": "#FFEBEE"
    },
    "ESTP": {
        "name": "방글핑",
        "emoji": "😄⚡",
        "image": "https://i.namu.wiki/i/Lq7NzVpYRJ4KEcXMJqOPRGYbCdK8FYzN3RmTpVxNJqLWbAcEXrMzKQRJpVqB7CzJ8NDpJqQ5HmFvK1XnPyOpAQ.webp",
        "description": "활발하고 즉흥적인 너! 늘 웃음 가득한 방글핑과 환상의 짝꿍!",
        "personality": "활발한 에너자이저",
        "fact": "😄 항상 방글방글 웃는 긍정 에너지 폭발 티니핑!",
        "quote": "방글방글~ 신난다!",
        "color": "#FF9800",
        "bg_color": "#FFF3E0"
    },
    "ESFP": {
        "name": "베베핑",
        "emoji": "🎀🌟",
        "image": "https://i.namu.wiki/i/VqXR8NzKYJlMpCJqOzYG_RJBdK7FYzN2RmTpVxNJqLWbAcEXrMzKQRJpVqB7CzJ8NDpJqQ5HmFvK1XnPyOpAQ.webp",
        "description": "사랑스럽고 분위기 메이커인 너! 귀여움 폭발 베베핑과 딱이야~",
        "personality": "분위기 메이커 스타",
        "fact": "🎀 깜찍 발랄 귀여움의 끝판왕! 베베핑은 모두의 사랑둥이~",
        "quote": "베베~ 귀엽지?",
        "color": "#E91E63",
        "bg_color": "#FCE4EC"
    }
}

# MBTI별 한국 인구 비율 (참고 데이터)
mbti_stats = {
    "ISFJ": 13.6, "ESFJ": 12.8, "ISTJ": 11.2, "ENFP": 9.5,
    "ESTJ": 8.4, "ISFP": 7.9, "ESFP": 7.1, "INFP": 6.3,
    "ENFJ": 5.4, "ISTP": 4.8, "ESTP": 4.2, "INTP": 3.5,
    "INFJ": 2.8, "ENTP": 2.5, "INTJ": 1.5, "ENTJ": 0.5
}

# 케미 점수 계산 함수
def calculate_chemistry(mbti):
    """MBTI 기반 케미 점수 계산 (재현 가능하도록 시드 고정)"""
    random.seed(sum(ord(c) for c in mbti))
    base_score = random.randint(85, 99)
    
    # 세부 점수
    scores = {
        "💖 사랑 케미": random.randint(80, 100),
        "🎮 놀이 케미": random.randint(80, 100),
        "🗣️ 대화 케미": random.randint(80, 100),
        "🌟 영혼 케미": random.randint(80, 100),
        "🎁 선물 케미": random.randint(80, 100)
    }
    return base_score, scores

# 타이틀
st.markdown("<h1 style='text-align: center;'>🌸💖 MBTI 티니핑 추천 💖🌸</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FF69B4;'>✨ 너에게 어울리는 티니핑은 누구일까? ✨</h3>", unsafe_allow_html=True)
st.markdown("---")

# 소개 메시지
st.markdown("""
<div style='text-align: center; background: linear-gradient(135deg, #FFE5F1 0%, #FFF0F5 100%); 
            padding: 20px; border-radius: 15px;'>
    <h4>🎀 안녕! 나는 티니핑 매칭 요정이야~ 🧚‍♀️</h4>
    <p>너의 MBTI를 알려주면 💌<br>
    너랑 찰떡궁합인 티니핑 친구와 <b>케미 점수</b>까지 알려줄게! 💕</p>
</div>
""", unsafe_allow_html=True)

st.markdown("###")

# 탭으로 구성
tab1, tab2 = st.tabs(["🎀 티니핑 추천받기", "📊 MBTI 통계 차트"])

with tab1:
    # MBTI 선택
    st.markdown("### 🌟 너의 MBTI를 선택해줘! 🌟")
    
    select_mode = st.radio(
        "선택 방법 🎯",
        ["🎀 한 번에 선택하기", "🔍 하나씩 골라보기"],
        horizontal=True
    )
    
    if select_mode == "🎀 한 번에 선택하기":
        mbti_list = ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
                     "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]
        mbti = st.selectbox("✨ 너의 MBTI는? ✨", mbti_list)
    else:
        col1, col2 = st.columns(2)
        with col1:
            ei = st.radio("🗣️ 외향/내향", ["E (외향) 🎉", "I (내향) 🌙"])
            sn = st.radio("👀 감각/직관", ["S (감각) 🌿", "N (직관) ✨"])
        with col2:
            tf = st.radio("🧠 사고/감정", ["T (사고) 🧊", "F (감정) 💖"])
            jp = st.radio("📅 판단/인식", ["J (계획) 📋", "P (즉흥) 🎲"])
        mbti = ei[0] + sn[0] + tf[0] + jp[0]
    
    st.markdown("###")
    
    # 추천 버튼
    if st.button("💝 내 티니핑 친구 찾아줘! 💝", use_container_width=True):
        result = tinyping_data[mbti]
        total_score, detail_scores = calculate_chemistry(mbti)
        
        st.balloons()
        
        # 결과 카드
        st.markdown(f"""
        <div style='text-align: center; background: {result["bg_color"]}; 
                    padding: 30px; border-radius: 20px; border: 3px dashed {result["color"]};'>
            <h2>🎊 너의 MBTI는 <span style='color:{result["color"]}'>{mbti}</span> 🎊</h2>
            <h1 style='font-size: 70px; margin: 20px 0;'>{result["emoji"]}</h1>
            <h1 style='color: {result["color"]};'>✨ {result["name"]} ✨</h1>
            <h3 style='color: {result["color"]};'>💫 {result["personality"]} 💫</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("###")
        
        # 이미지 표시 (이미지 로딩 실패 시 대체)
        try:
            st.image(result["image"], caption=f"🎀 {result['name']} 🎀", use_container_width=True)
        except:
            st.markdown(f"""
            <div style='text-align: center; font-size: 150px; padding: 30px;
                       background: {result["bg_color"]}; border-radius: 20px;'>
                {result["emoji"]}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("###")
        
        # 설명 카드
        st.markdown(f"""
        <div style='background: white; padding: 20px; border-radius: 15px; 
                    border-left: 5px solid {result["color"]};'>
            <p style='font-size: 18px;'>💌 {result["description"]}</p>
            <p style='font-size: 16px;'><b>🌟 비밀 정보:</b> {result["fact"]}</p>
            <p style='font-size: 16px; font-style: italic; color: {result["color"]};'>
                💬 "{result["quote"]}"
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("###")
        
        # 💖 케미 점수 섹션
        st.markdown("## 💖 티니핑과의 케미 점수 💖")
        
        # 총점
        st.markdown(f"""
        <div style='text-align: center; background: linear-gradient(135deg, #FFE5F1, #E1F5FE);
                    padding: 25px; border-radius: 20px;'>
            <h3>🏆 종합 케미 점수 🏆</h3>
            <h1 style='font-size: 80px; color: {result["color"]}; margin: 10px;'>
                {total_score}점
            </h1>
            <p style='font-size: 18px;'>{'🌟' * (total_score // 20)} </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("###")
        
        # 세부 케미 점수 (프로그레스 바)
        st.markdown("### 📊 세부 케미 분석")
        for category, score in detail_scores.items():
            st.markdown(f"**{category}**: {score}점")
            st.progress(score / 100)
        
        st.markdown("###")
        
        # 케미 평가 메시지
        if total_score >= 95:
            msg = "🌟 완벽한 운명의 짝꿍! 💯 환상의 케미야~"
            emoji = "💖💖💖"
        elif total_score >= 90:
            msg = "✨ 정말 잘 어울리는 베스트 프렌드! 🎀"
            emoji = "💖💖"
        else:
            msg = "💕 좋은 친구가 될 수 있어! 함께 행복해지자~"
            emoji = "💖"
        
        st.markdown(f"""
        <div style='text-align: center; background: {result["bg_color"]};
                    padding: 20px; border-radius: 15px;'>
            <h2>{emoji}</h2>
            <h3>{msg}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("###")
        st.success(f"🎁 {result['name']}와 함께 행복한 하루 보내세요! 💖")

with tab2:
    st.markdown("## 📊 MBTI 통계 차트 📊")
    st.markdown("### 🇰🇷 한국인 MBTI 분포 (%)")
    
    # 데이터프레임 생성
    df = pd.DataFrame({
        'MBTI': list(mbti_stats.keys()),
        '비율(%)': list(mbti_stats.values())
    })
    df = df.sort_values('비율(%)', ascending=False)
    
    # 바 차트
    st.bar_chart(df.set_index('MBTI'), color="#FF69B4")
    
    st.markdown("###")
    
    # 상위 3개 / 하위 3개
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏆 가장 많은 MBTI TOP 3")
        top3 = df.head(3)
        for idx, row in top3.iterrows():
            tinyping_name = tinyping_data[row['MBTI']]['name']
            emoji = tinyping_data[row['MBTI']]['emoji']
            st.markdown(f"**{row['MBTI']}** {emoji} → {tinyping_name} ({row['비율(%)']}%)")
    
    with col2:
        st.markdown("### 💎 가장 희귀한 MBTI TOP 3")
        bottom3 = df.tail(3).iloc[::-1]
        for idx, row in bottom3.iterrows():
            tinyping_name = tinyping_data[row['MBTI']]['name']
            emoji = tinyping_data[row['MBTI']]['emoji']
            st.markdown(f"**{row['MBTI']}** {emoji} → {tinyping_name} ({row['비율(%)']}%)")
    
    st.markdown("###")
    st.info("💡 한국인 MBTI 분포 참고 데이터입니다. 실제 통계와는 차이가 있을 수 있어요!")
    
    # 전체 목록 표
    st.markdown("### 📋 전체 MBTI별 티니핑 목록")
    full_df = pd.DataFrame([
        {
            "MBTI": k,
            "티니핑": f"{v['emoji']} {v['name']}",
            "성격": v['personality'],
            "비율(%)": mbti_stats[k]
        }
        for k, v in tinyping_data.items()
    ])
    st.dataframe(full_df, use_container_width=True, hide_index=True)

# 사이드바
with st.sidebar:
    st.markdown("## 🎀 티니핑 도감 📖")
    st.markdown("---")
    for mbti_type, info in tinyping_data.items():
        st.markdown(f"**{mbti_type}** {info['emoji']}")
        st.markdown(f"→ {info['name']}")
        st.markdown("")

# 푸터
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>💕 Made with Streamlit 🎀 | 당곡고등학교 AI 학습 도우미 🌸</p>
    <p>🌟 캐치! 티니핑 © SAMG Entertainment 🌟</p>
</div>
""", unsafe_allow_html=True)

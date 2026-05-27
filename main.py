import streamlit as st

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
        "description": "차갑고 시크하지만 속은 깊은 매력! 자기 세계가 확실한 너에게 딱이야~",
        "personality": "냉철한 전략가",
        "fact": "❄️ 차가운 마음의 티니핑! 시크함 뒤에 숨겨진 진심이 매력이야~",
        "color": "#4A90E2",
        "bg_color": "#E3F2FD"
    },
    "INTP": {
        "name": "아잉핑",
        "emoji": "🤔💭",
        "description": "엉뚱하고 호기심 가득한 너! 알쏭달쏭 아잉핑과 환상의 콤비~",
        "personality": "엉뚱한 호기심쟁이",
        "fact": "💭 '아잉~' 하면서 헷갈리게 만드는 매력의 소유자!",
        "color": "#9B59B6",
        "bg_color": "#F3E5F5"
    },
    "ENTJ": {
        "name": "마음핑",
        "emoji": "👑💪",
        "description": "리더십 만렙! 강한 카리스마의 마음핑과 너무 잘 어울려~",
        "personality": "당당한 리더",
        "fact": "💪 강한 마음의 힘을 가진 티니핑! 모두를 이끄는 카리스마~",
        "color": "#E74C3C",
        "bg_color": "#FFEBEE"
    },
    "ENTP": {
        "name": "악동핑",
        "emoji": "😈✨",
        "description": "장난기 가득! 아이디어 뱅크인 너와 악동핑은 환상의 짝꿍!",
        "personality": "재치만점 트러블메이커",
        "fact": "😈 장난치는 걸 제일 좋아하는 악동! 하지만 미워할 수 없어~",
        "color": "#F39C12",
        "bg_color": "#FFF3E0"
    },
    "INFJ": {
        "name": "하츄핑",
        "emoji": "💗🌷",
        "description": "따뜻하고 사랑이 넘치는 너! 사랑의 요정 하츄핑과 영혼의 단짝!",
        "personality": "사랑둥이 힐러",
        "fact": "💗 사랑의 마음을 전해주는 메인 티니핑! 모두를 행복하게 해~",
        "color": "#FF69B4",
        "bg_color": "#FCE4EC"
    },
    "INFP": {
        "name": "라라핑",
        "emoji": "🎵💜",
        "description": "감수성 풍부한 예술가 타입! 음악을 사랑하는 라라핑과 찰떡이야~",
        "personality": "감성충만 아티스트",
        "fact": "🎵 노래와 음악을 사랑하는 티니핑! 감성 폭발 매력~",
        "color": "#B19CD9",
        "bg_color": "#F3E5F5"
    },
    "ENFJ": {
        "name": "해핑",
        "emoji": "☀️😊",
        "description": "밝고 따뜻한 너의 에너지! 햇살 같은 해핑과 너무 잘 어울려~",
        "personality": "햇살같은 행복전도사",
        "fact": "☀️ 햇살처럼 따뜻하게 모두를 비춰주는 천사 티니핑~",
        "color": "#FFD700",
        "bg_color": "#FFFDE7"
    },
    "ENFP": {
        "name": "바로핑",
        "emoji": "🌈🎉",
        "description": "에너지 폭발 자유로운 영혼! 변신의 달인 바로핑과 환상의 콤비!",
        "personality": "자유로운 변신요정",
        "fact": "🌈 '바로 바로!' 다양하게 변신하는 만능 티니핑~",
        "color": "#FF6B9D",
        "bg_color": "#FCE4EC"
    },
    "ISTJ": {
        "name": "꾸래핑",
        "emoji": "📚🎀",
        "description": "성실하고 책임감 강한 너! 꼼꼼한 꾸래핑과 환상의 짝꿍이야~",
        "personality": "성실한 모범생",
        "fact": "📚 매일 꾸준히 무언가를 하는 성실 끝판왕 티니핑!",
        "color": "#8B7355",
        "bg_color": "#EFEBE9"
    },
    "ISFJ": {
        "name": "포실핑",
        "emoji": "🧸💕",
        "description": "포근하고 다정한 너! 따뜻한 마음의 포실핑과 닮은 매력이야~",
        "personality": "포근한 힐링요정",
        "fact": "🧸 포근포근한 마음으로 친구들을 챙겨주는 다정한 티니핑~",
        "color": "#FFB6C1",
        "bg_color": "#FCE4EC"
    },
    "ESTJ": {
        "name": "똑똑핑",
        "emoji": "🎓📖",
        "description": "체계적이고 야무진 너! 똑똑한 친구 똑똑핑과 너무 잘 어울려~",
        "personality": "야무진 우등생",
        "fact": "🎓 모르는 게 없는 척척박사 티니핑! 똑소리 나는 매력~",
        "color": "#27AE60",
        "bg_color": "#E8F5E9"
    },
    "ESFJ": {
        "name": "정의핑",
        "emoji": "⚖️💖",
        "description": "정의롭고 사교적인 너! 모두를 챙기는 정의핑과 찰떡궁합!",
        "personality": "정의로운 히어로",
        "fact": "⚖️ 옳고 그름을 가리는 정의의 사도 티니핑! 든든해~",
        "color": "#FF4757",
        "bg_color": "#FFEBEE"
    },
    "ISTP": {
        "name": "샤샤핑",
        "emoji": "✂️🤍",
        "description": "쿨하고 손재주 좋은 너! 시크한 매력의 샤샤핑과 닮았어~",
        "personality": "쿨한 만능 해결사",
        "fact": "✂️ 자기 일을 야무지게 해내는 쿨한 매력의 티니핑!",
        "color": "#34495E",
        "bg_color": "#ECEFF1"
    },
    "ISFP": {
        "name": "딸기핑",
        "emoji": "🍓💝",
        "description": "조용하지만 사랑스러운 너! 달콤한 딸기핑과 너무 잘 어울려~",
        "personality": "달콤상냥 매력쟁이",
        "fact": "🍓 딸기처럼 달콤하고 새콤한 매력의 티니핑~",
        "color": "#FF1744",
        "bg_color": "#FFEBEE"
    },
    "ESTP": {
        "name": "방글핑",
        "emoji": "😄⚡",
        "description": "활발하고 즉흥적인 너! 늘 웃음 가득한 방글핑과 환상의 짝꿍!",
        "personality": "활발한 에너자이저",
        "fact": "😄 항상 방글방글 웃는 긍정 에너지 폭발 티니핑!",
        "color": "#FF9800",
        "bg_color": "#FFF3E0"
    },
    "ESFP": {
        "name": "베베핑",
        "emoji": "🎀🌟",
        "description": "사랑스럽고 분위기 메이커인 너! 귀여움 폭발 베베핑과 딱이야~",
        "personality": "분위기 메이커 스타",
        "fact": "🎀 깜찍 발랄 귀여움의 끝판왕! 베베핑은 모두의 사랑둥이~",
        "color": "#E91E63",
        "bg_color": "#FCE4EC"
    }
}

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
    너랑 찰떡궁합인 티니핑 친구를 찾아줄게! 💕</p>
</div>
""", unsafe_allow_html=True)

st.markdown("###")

# MBTI 선택
st.markdown("### 🌟 너의 MBTI를 선택해줘! 🌟")

# 선택 방법 두 가지 제공
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
    
    st.balloons()
    
    st.markdown(f"""
    <div style='text-align: center; background: {result["bg_color"]}; 
                padding: 30px; border-radius: 20px; border: 3px dashed {result["color"]};'>
        <h2>🎊 너의 MBTI는 <span style='color:{result["color"]}'>{mbti}</span> 🎊</h2>
        <h1 style='font-size: 70px; margin: 20px 0;'>{result["emoji"]}</h1>
        <h1 style='color: {result["color"]};'>✨ {result["name"]} ✨</h1>
        <h3 style='color: {result["color"]};'>💫 {result["personality"]} 💫</h3>
        <p style='font-size: 18px; margin-top: 20px; background: white; padding: 15px; border-radius: 10px;'>
            💌 {result["description"]} 💌
        </p>
        <p style='font-size: 16px; margin-top: 15px; background: white; padding: 15px; border-radius: 10px;'>
            <b>🌟 티니핑 비밀 정보 🌟</b><br>{result["fact"]}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("###")
    st.success(f"🎁 {result['name']}와 함께 행복한 하루 보내세요! 💖")
    
    st.markdown("""
    <div style='text-align: center; margin-top: 20px; background-color: #FFF0F5; 
                padding: 15px; border-radius: 10px;'>
        <p>🌈 친구들에게도 공유해서 어떤 티니핑이 나오는지 알려줘! 🎀<br>
        💕 다른 MBTI도 궁금하면 다시 선택해봐~ 💕</p>
    </div>
    """, unsafe_allow_html=True)

# 사이드바 - 모든 캐릭터 미리보기
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

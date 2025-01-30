import streamlit as st
# Firm details
QUIZ_TITLE = "WOFA 2025 ESG Quiz"
FIRM_NAME = "K Venkatachalam Aiyer & Co."
LOGO_PATH = "logo.png"  # Ensure the logo is in the same folder as this script

# Display title, firm name, and logo
col1, col2 = st.columns([1, 4])  # Create two columns for alignment

with col1:
    st.image(LOGO_PATH, width=100)  # Adjust width as needed

with col2:
    st.title(QUIZ_TITLE)
    st.write(f"**{FIRM_NAME}**")  # Firm name in bold

# Dictionary containing 10 different quizzes
quizzes = {
    "Manufacturing and Heavy Industries": [
        {"question": "Does the company use sustainably sourced raw materials?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Are there measures to monitor and reduce greenhouse gas emissions?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Does the company recycle or reuse industrial waste?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Is renewable energy used in the company's operations?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Are employee safety measures in line with industry standards?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Does the company consult with local communities for new projects?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Is worker training provided for new technologies?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Does the company support local job creation?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Are ESG policies integrated into procurement practices?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Is there independent oversight of the company's environmental policies?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Does the company disclose its compliance with local and global ESG laws?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Are board members trained on ESG-specific risks?", "options": ["Yes", "No"], "answer": "Yes"},
        
        
    ],
    "Technology and IT Services": [
        {"question": "Are data centers powered by renewable energy?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Does the company have an e-waste recycling policy?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Are carbon emissions from IT opera ons measured and reported?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Is there a policy to procure energy-eﬃcient hardware?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Does the company provide cybersecurity training for employees?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Are diversity and inclusion goals ac vely monitored and reported?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Does the company contribute to digital literacy programs in underserved areas?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Are employees oﬀered flexible work arrangements?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Are data privacy prac ces audited regularly?", "options": ["Yes", "No"], "answer": "Yes"},
        {"question": "Is there a whistleblower policy for unethical IT practices?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Does the company disclose ESG compliance in its financial reports?", "options": ["Yes", "No"], "answer": "Yes"}, 
        {"question": "Are ethical AI practices part of the company's policies?", "options": ["Yes", "No"], "answer": "Yes"},   
    ],
    "Healthcare and Pharmaceuticals": [
    {"question": "Are biohazardous wastes disposed of in compliance with environmental laws?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company use sustainable materials for packaging?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are measures in place to minimize water usage in production?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company invest in R&D for green production methods?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are medicines made affordable for low-income communities?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is informed consent obtained for all clinical trials?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are employee wellness programs in place?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company engage with local healthcare initiatives?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there transparency in drug safety reporting?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company prevent unethical marketing practices?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are ESG risks integrated into the company's strategic decision-making?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are there regular compliance audits with international healthcare regulations?", "options": ["Yes", "No"], "answer": "Yes"},
],

    "Real Estate and Construction": [
    {"question": "Are energy-efficient materials used in construction projects?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company adhere to green building standards (e.g., LEED, BREEAM)?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are biodiversity impacts assessed before starting new projects?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is rainwater harvesting implemented in company properties?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are construction workers provided with safety training and equipment?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company develop affordable housing projects?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are displaced communities compensated or resettled fairly?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are labor rights audited across all subcontractors?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are environmental impact assessments disclosed to stakeholders?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company adhere to anti-corruption policies in land acquisition?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are project delays or changes communicated transparently?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there board oversight of ESG integration in construction practices?", "options": ["Yes", "No"], "answer": "Yes"},
],

"Energy Industry (Oil and Gas)": [
    {"question": "Does the company measure and disclose GHG emissions (Scope 1, 2, and 3)?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are methane emissions from extraction and transportation monitored and reduced?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there a strategy for transitioning to cleaner or renewable energy sources?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are environmental impact assessments conducted before initiating extraction projects?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company have a policy for responsible flaring and venting practices?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are spill prevention measures and rapid response systems in place?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company engage in carbon offsetting or carbon capture and storage (CCS)?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are water resources managed sustainably during extraction and refining processes?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are hazardous wastes (e.g., drilling muds, refinery byproducts) handled responsibly?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there a plan to decommission and remediate retired facilities or fields?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are local communities consulted before initiating exploration or drilling projects?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company provide community benefits (e.g., schools, health facilities) in operational areas?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are employees and contractors trained in health, safety, and environmental (HSE) protocols?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company ensure fair labor practices in its operations and supply chain?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are there measures in place to reskill workers impacted by a transition to renewables?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company have a diversity, equity, and inclusion policy?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are grievance mechanisms available for stakeholders to report social or environmental concerns?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company offer financial transparency on royalties and taxes paid to governments?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are there systems to monitor and address the impact of operations on Indigenous populations?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company have safety protocols to minimize workplace accidents?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there a dedicated ESG committee at the board level?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are ESG metrics integrated into executive compensation plans?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company comply with international oil and gas industry standards (e.g., API, IPIECA)?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are ESG risks, including stranded assets, assessed and disclosed?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company adhere to anti-bribery and corruption laws in global operations?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are stakeholders provided with regular ESG performance updates?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are partnerships pursued to develop cleaner extraction and refining technologies?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there a whistleblower policy in place for unethical practices?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are climate-related risks aligned with frameworks like TCFD in financial disclosures?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company disclose tax and royalty contributions on a country-by-country basis?", "options": ["Yes", "No"], "answer": "Yes"},
],

    "Electricity Industry": [
    {"question": "Does the company measure and disclose GHG emissions from power generation (Scope 1, 2, and 3)?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are renewable energy sources (e.g., solar, wind, hydropower) integrated into the energy mix?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there a commitment to phase out coal or fossil fuel-based power plants?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are energy efficiency measures implemented across power generation and transmission systems?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are carbon capture and storage (CCS) technologies used for thermal power plants?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are emissions from transmission and distribution losses actively monitored and minimized?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is biodiversity protected during the construction of power generation facilities?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company recycle and manage waste from power plants (e.g., ash, nuclear waste)?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are water-efficient cooling systems implemented in thermal plants?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are environmental compliance certifications obtained for all power generation facilities?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company ensure universal access to electricity for underserved communities?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are safety measures in place for workers maintaining high-voltage equipment?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company promote energy affordability and avoid discriminatory pricing?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are local communities engaged in the planning and construction of power projects?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are there programs to train employees in new energy technologies (e.g., smart grids, renewables)?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company ensure diversity and inclusion in its workforce, including leadership?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are customers educated about energy efficiency and demand-side management?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company compensate communities affected by power plant operations?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are there systems to prevent workplace accidents in high-risk environments?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company collaborate with schools or NGOs to promote STEM education?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are ESG risks integrated into the company’s strategic planning?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there a board-level committee overseeing sustainability goals?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are ESG-related disclosures aligned with global standards like GRI, SASB, or TCFD?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company have a formal policy to prevent corruption and fraud?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are executive incentives tied to achieving renewable energy or carbon reduction goals?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company adhere to regulations on grid reliability and renewable integration?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is there a whistleblower mechanism for reporting ethical breaches?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are supply chain partners audited for ESG compliance?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are financial risks related to climate change disclosed in reports?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company publish stakeholder feedback and grievance resolution data?", "options": ["Yes", "No"], "answer": "Yes"},
],
    "ESG Reporting Assessment": [
    {"question": "Does the company have policies to reduce greenhouse gas (GHG) emissions?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company regularly monitor and report its energy consumption?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Has the company implemented initiatives to reduce water usage?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company have a waste management policy, including recycling and disposal of hazardous waste?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are there measures in place to minimize the environmental impact of the company’s supply chain?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company invest in renewable energy sources or energy-efficient technologies?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are environmental risks assessed as part of the company’s overall risk management strategy?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company have a diversity and inclusion policy for employees?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are employee health, safety, and well-being actively monitored and promoted?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company engage in community development or social responsibility initiatives?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are labor practices in the company’s operations and supply chain regularly reviewed for compliance with laws and ethical standards?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company provide training and development programs for employees?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are customer data privacy and security measures in place?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company engage with stakeholders (e.g., employees, customers, communities) to address their concerns?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are there policies in place to prevent conflicts of interest and unethical behavior?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company have a code of conduct that employees are required to follow?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Is the company’s executive compensation aligned with long-term value creation?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are financial and non-financial disclosures made transparently and regularly?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Does the company conduct audits to ensure compliance with governance policies and regulations?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Are whistleblower mechanisms in place to report unethical practices?", "options": ["Yes", "No"], "answer": "Yes"},
],
   "AI Knowledge Quiz": [
    {"question": "What does AI stand for?", "options": ["A) Automated Intelligence", "B) Artificial Intelligence", "C) Algorithmic Intelligence", "D) Automated Integration"], "answer": "B) Artificial Intelligence"},
    {"question": "Which of the following is an example of supervised learning?", "options": ["A) Clustering of data points into groups", "B) Predicting house prices based on historical data with known labels", "C) Identifying anomalies in network traffic", "D) Machine-generated artwork from scratch"], "answer": "B) Predicting house prices based on historical data with known labels"},
    {"question": "Which of the following is NOT an example of natural language processing (NLP)?", "options": ["A) Text classification", "B) Speech recognition", "C) Object detection in images", "D) Machine translation"], "answer": "C) Object detection in images"},
    {"question": "Which of these is the primary function of a neural network in AI?", "options": ["A) To optimize resources in an organization", "B) To recognize patterns and learn from data", "C) To create data visualizations", "D) To write software code"], "answer": "B) To recognize patterns and learn from data"},
    {"question": "What is reinforcement learning primarily used for?", "options": ["A) Learning from data labeled by humans", "B) Improving decision-making through trial and error", "C) Classifying text into categories", "D) Identifying patterns in time series data"], "answer": "B) Improving decision-making through trial and error"},
    {"question": "In which field is convolutional neural networks (CNNs) commonly applied?", "options": ["A) Natural Language Processing (NLP)", "B) Image and video recognition", "C) Time-series forecasting", "D) Reinforcement learning"], "answer": "B) Image and video recognition"},
    {"question": "What is the Turing Test designed to evaluate?", "options": ["A) Whether a machine can perform calculations faster than a human", "B) Whether a machine can pass as human in conversation", "C) Whether an AI can write original poetry", "D) Whether an AI can predict the stock market"], "answer": "B) Whether a machine can pass as human in conversation"},
    {"question": "What does GPT stand for in the context of AI?", "options": ["A) General Programming Tool", "B) Generative Pretrained Transformer", "C) Graph Processing Technology", "D) Global Prediction Tool"], "answer": "B) Generative Pretrained Transformer"},
    {"question": "Which AI algorithm is commonly used in chatbots and virtual assistants?", "options": ["A) Decision trees", "B) Support vector machines (SVM)", "C) Recurrent neural networks (RNN)", "D) Genetic algorithms"], "answer": "C) Recurrent neural networks (RNN)"},
    {"question": "Deep learning is a subset of which type of machine learning?", "options": ["A) Reinforcement Learning", "B) Supervised Learning", "C) Unsupervised Learning", "D) Both supervised and unsupervised learning"], "answer": "D) Both supervised and unsupervised learning"},
],
}



# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_complete" not in st.session_state:
    st.session_state.quiz_complete = False
if "selected_quiz" not in st.session_state:
    st.session_state.selected_quiz = None

# App title
st.title("🎯WOFA 2025 ESG Quiz")

# Quiz Selection
if st.session_state.selected_quiz is None:
    st.subheader("Choose a Quiz Category:")
    quiz_choice = st.selectbox("Select a category:", list(quizzes.keys()))

    if st.button("Start Quiz"):
        st.session_state.selected_quiz = quiz_choice
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_complete = False
        st.rerun()

else:
    selected_quiz = quizzes[st.session_state.selected_quiz]

    if not st.session_state.quiz_complete:
        # Display question
        question_data = selected_quiz[st.session_state.current_question]

        st.subheader(f"Question {st.session_state.current_question + 1}")
        st.write(question_data["question"])

        # Answer options
        selected_option = st.radio("Choose your answer:", question_data["options"])

        # Submit button
        if st.button("Submit Answer"):
            if selected_option == question_data["answer"]:
                st.session_state.score += 1

            # Move to next question
            if st.session_state.current_question < len(selected_quiz) - 1:
                st.session_state.current_question += 1
            else:
                st.session_state.quiz_complete = True

            st.rerun()

    else:
        # Display final score
        st.subheader("Quiz Completed! 🎉")
        st.write(f"Your Score: **{st.session_state.score} / {len(selected_quiz)}**")

        # Retry button
        if st.button("Try Another Quiz"):
            st.session_state.selected_quiz = None
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_complete = False
            st.rerun()

from langchain.llms import GooglePalm
api_key = "AIzaSyAnDP1s8qubXbgfbcPtQ8ehqzOLpGrHilA"
llm = GooglePalm(google_api_key=api_key,temperature=0.6)
text = llm("give me some name for my AI & Data Science book")
print(text)
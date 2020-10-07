from fastapi import FastAPI
from nlp import NLP

# nlp = NLP()
app = FastAPI()
nlp = NLP()


TEST_STRING = """The work of an intellectual is  not to mould the political will of others; it is, through the analyses that he does in his own field, to re-examine evidence and assumptions, to shake up habitual ways of working and thinking, to dissipate conventional familiarities, to re-evaluate rules and institutions and to participate in the formation of a political will (where he has his role as citizen to play)."""


@app.get("/")
async def root():
    
    ret = nlp.chat_bot(TEST_STRING)
    return {"{Foucault}": ret}

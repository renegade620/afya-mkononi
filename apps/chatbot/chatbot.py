from sentence_transformers import SentenceTransformer, util
from .pregnancy_data import pregnancy_qa_data  # Import dataset


class PregnancyChatbot:
    def __init__(self):
        # Load pre-trained sentence transformer model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.questions = [item["question"] for item in pregnancy_qa_data]
        self.answers = [item["answer"] for item in pregnancy_qa_data]
        # Embed all questions in the dataset
        self.question_embeddings = self.model.encode(
            self.questions, convert_to_tensor=True
        )

    def get_response(self, user_question):
        """
        Finds the most similar question in the dataset to the user's question
        and returns the corresponding answer.
        """
        user_question_embedding = self.model.encode(
            user_question, convert_to_tensor=True
        )
        # Calculate cosine similarity between user question and all questions in the dataset
        cosine_scores = util.pytorch_cos_sim(
            user_question_embedding, self.question_embeddings
        )[0]
        # Find the index of the most similar question
        most_similar_index = cosine_scores.argmax()
        # Return the answer corresponding to the most similar question
        return self.answers[most_similar_index]

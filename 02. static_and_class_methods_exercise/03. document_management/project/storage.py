from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = [c for c in self.categories if c.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = self.get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        self.categories.remove([c for c in self.categories if c.id == category_id][0])

    def delete_topic(self, topic_id) -> None:
        self.topics.remove([t for t in self.topics if t.id == topic_id][0])

    def delete_document(self, document_id) -> None:
        self.documents.remove(self.get_document(document_id))

    def get_document(self, document_id):
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])

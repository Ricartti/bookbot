# My old answers version
# 
# Solution 2.2
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     print(text)
# def get_book_text(path):
#     with open(path) as f:
#         return f.read()
# main()
# 
# Solution 2.3
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     print(f"{num_words} words found in the document")
# def get_book_text(path):
#     with open(path) as f:
#         return f.read()
# def get_num_words(text):
#     words = text.split()
#     return len(words)
# main()

# Solution 2.4

# def get_characters(text):
#     dict = { }
#     new_text = text.lower()
#     words = new_text.split()
#     for single_word in words:
#         for character in single_word:
#             if character not in dict:
#                 dict[character] = 1
#             if character in dict:
#                 dict[character] += 1
#     return dict


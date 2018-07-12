# def word_in_pos(x, y):
#     word = x
#     for word in y:
#         if word == "__" + str(x) + "__":
#             print word
#             return word
#         else:
#             print "none"
#             return None

def word_in_pos(answer_number, split_question):
    number = answer_number
    for number in split_question:
        if number == "__" + str(answer_number) + "__":
            print number
            return number
        else:
            print "none"
            return None

word_in_pos(1, ["__1__", "__2__", "__3__"])
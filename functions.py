def tokenization_white_spaces(text):
    """
    Χωρίζει το κείμενο σε λέξεις με βάση τους κενούς χαρακτήρες.
    Parameters:
    text(str): Αν το κείμενο είναι string το χωρίζει σε λέξεις
    Return:
    list: Επιστρέφει το κείμενο σε λέξεις.
    """
    if isinstance(text, str):
        text = text.split()
        return text

def remove_punctuation(puncts):
    """
    Αφαιρεί τα σημεία στίξης από τις λέξεις μιας λίστας.
    :param:
    puncts(list): Δημιουργεί μια νέα κενή λίστα στην οποία προστίθενται οι λέξεις χωρίς τα σημεία στίξης.
    :return:
    list:Επιστρέφει μια νέα λίστα χωρίς τα σημεία στίξης από τις λέξεις.
    """
    if isinstance(puncts, list):
        new_text = []
        for punct in puncts:
            puncts = punct.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace("'", "").replace("˙", "")
            new_text.append(puncts)
        return new_text


def remove_stop_words(input,  stop_words = ["shan't", 'into', 'has', "weren't", 'ours', 'him', 'this', 'those', 'an', 've', 'hadn', 'wasn', 'same', 'doing', 'just', 'won', 'the', 'while', "needn't", 'weren', 'wouldn', "mustn't", 'out', 'any', 'on', 'these', 'against', 'm', 'here', 'again', 'have', 'in', 'yourself', 'further', 'who', 'haven', 'by', 'each', 'at', "it's", "isn't", 'a', 'i', 'its', "won't", 'are', 'once', 'be', 'than', 'that', 'all', 'below', "hadn't", 'my', "couldn't", 'isn', "you'd", 'as', 'can', 's', 'been', 'before', 'y', 'she', 'do', 'we', 'until', 't', 'nor', "hasn't", 'd', 'ma', 'why', 'after', 'don', 'down', 'shouldn', "didn't", 'were', 'herself', 'under', 'during', 'only', 'most', 'very', 'their', 'is', 'o', 'about', 'had', 'them', 'aren', 'doesn', 'your', 'such', 'now', "you've", 'between', 'does', 'couldn', 'needn', 'there', 'our', 'so', 'off', 'for', 'because', 'few', 'll', 'where', 'of', 'they', 'hasn', "mightn't", 'did', 'mightn', 'it', 'some', 'yourselves', "wasn't", 'will', 'yours', "that'll", 'how', "doesn't", "she's", 'up', 'or', 'then', 'more', "shouldn't", 'having', 'from', 'over', 'ain', "should've", 'was', "don't", "haven't", 'too', "wouldn't", 'if', 'didn', 'but', 'itself', 'should', 'shan', 'which', 'both', 'not', 'through', 're', 'other', 'her', 'theirs', "you're", 'himself', 'myself', 'he', 'what', 'being', "aren't", 'when', 'and', 'you', 'whom', 'am', 'to', 'own', 'ourselves', 'mustn', 'with', "you'll", 'above', 'hers', 'themselves', 'his', 'no', 'me']):
    """
    Παίρνει δύο ορίσματα και αφαιρεί τα stop words από τη λίστα, τα οποία είναι από πριν καθορισμένα.
    Parameters:
    input(list), stop_words(list): Δημιουργείται νέα κενή λίστα στην οποία προστίθενται οι λέξεις που δεν ανήκουν στη λίστα stop_words με χρήση for loop.
    :return:
    list: Επιστρέφει μια λίστα με τις λέξεις που δεν είναι stop words.
    """
    if isinstance(input, list):
        new_input = []
        for i in input:
            if i not in stop_words:
                new_input.append(i)
        return new_input

def check_palindrome(words):
    """
    Ελέγχει αν το string είναι σε καρκινική γραφή.
    Parameters:
     words(str): Το όρισμα ελέγχεται αν είναι string και αν ισοδυναμεί με την αντίστροφη λέξη.
    return:
    boolean: Επιστρέφει True αν είναι σε καρκινική γραφή διαφορετικά False.
    """
    if isinstance(words, str):
        reverse_words = words[::-1]
        if words == reverse_words:
            return True
        else:
            return False

def palindrome_words(word):
    """
    Δίνει τις λέξεις που είναι σε καρκινική γραφή.
    Parameters:
    word(list): Αν το όρισμα είναι λίστα τότε για κάθε λέξη στη λίστα ελέγχεται αν είναι σε καρκινική γραφή.
    return:
    set: Επιστρέφει τις μοναδικές λέξεις σε καρκινική γραφή.
    """
    if isinstance(word, list):
        palindrome_words = []
        for i in word:
            i = i.lower()
            if check_palindrome(i):
                palindrome_words.append(i)
        return set(palindrome_words)

text_input="At noon, Anna and I launched our kayak into the calm lake, eager to explore. The water was perfectly level, reflecting the clear blue sky above like a mirror. \n As we paddled along, the stunning scenery made us both exclaim, 'Wow!' 'Can you believe how beautiful this is?'    Anna asked, her eyes wide with awe. It was a moment we would never forget."

print(f"Επεξεργασμένο κείμενο:", remove_stop_words(remove_punctuation(tokenization_white_spaces(text_input))))
print(f"Καρκινικές λέξεις: ", palindrome_words(remove_stop_words(remove_punctuation(tokenization_white_spaces(text_input)))))




import nltk

"""
Noun Phrase Extractor

This script defines a Noun Phrase Extractor object
that uses the Brown corpus to tag parts of speech,
simplifies the tags for parts of speech, and extracts
noun phrases from the tagged sentence.

Based on the script here by Shlomi Babluki:
http://thetokenizer.com/2013/05/09/efficient-way-to-extract-the-main-topics-of-a-sentence/
"""

print("Importing Brown corpus: this may take a while...")
from nltk.corpus import brown

# Hierarchy of taggers:
# http://www.nltk.org/book/ch05.html
brown_tagger = brown.tagged_sents(categories='news')
regexp_tagger = nltk.RegexpTagger(
    [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
     (r'(-|:|;)$', ':'),
     (r'\'*$', 'MD'),
     (r'(The|the|A|a|An|an)$', 'AT'),
     (r'.*able$', 'JJ'),
     (r'^[A-Z].*$', 'NNP'),
     (r'.*ness$', 'NN'),
     (r'.*ly$', 'RB'),
     (r'.*ing$', 'VBG'),
     (r'.*ed$', 'VBD'),
     (r'.*es$', 'VBZ'),
     (r'.*ould$', 'MD'),
     (r'.*\'s$', 'NN$'),
     (r'.*s$', 'NNS'),
     (r'.*', 'NN')
])
unigram_tagger = nltk.UnigramTagger(brown_tagger, backoff=regexp_tagger)
bigram_tagger = nltk.BigramTagger(brown_tagger, backoff=unigram_tagger)
print("Finished.")


# Define a context-free grammar
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
cfg = {}
cfg["NNP+NNP"] = "NNP" # proper noun singular: 2->1
cfg["NN+NN"] = "NNI" # noun singular or mass: 2->1
cfg["NNI+NN"] = "NNI" # noun singular or mass: n->n-1
cfg["JJ+JJ"] = "JJ" # adjective: 2->1
cfg["JJ+NN"] = "NNI" # adjective + noun: 2->1


class NounPhraseExtractor(object):
    """
    Noun Phrase Extractor.

    Tag a sentence with POS using the Brown corpus, 
    simplify the POS tagging schema used,
    and use the POS tags to extract noun phrases.
    """
    def __init__(self, sentence):
        self.sentence = sentence

    def _tokenize_sentence(self, sentence):
        """
        Split sentence into single words/tokens
        """
        # http://www.nltk.org/api/nltk.tokenize.html
        # http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.treebank.TreebankWordTokenizer
        tokens = nltk.word_tokenize(sentence)
        return tokens

    def _normalize_tags(self, tagged):
        """
        Normalize (simplify) the Brown corpus POS 
        tags ("NN", "NN-PL", "NNS" > "NN")

        Also see:
        https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
        """
        n_tagged = []
        for t in tagged:
            if t[1] == "NP-TL" or t[1] == "NP":
                n_tagged.append((t[0], "NNP"))
                continue
            if t[1].endswith("-TL"):
                n_tagged.append((t[0], t[1][:-3]))
                continue
            if t[1].endswith("S"):
                n_tagged.append((t[0], t[1][:-1]))
                continue
            n_tagged.append((t[0], t[1]))
        return n_tagged

    def extract(self):
        """Extract the main topics from the sentence"""
        tokens  = self._tokenize_sentence(self.sentence)
        tags    = self._normalize_tags(bigram_tagger.tag(tokens))

        merge = True
        while merge:
            merge = False
            for x in range(0, len(tags) - 1):
                t1 = tags[x]
                t2 = tags[x + 1]
                key = "%s+%s" % (t1[1], t2[1])
                value = cfg.get(key, '')
                if value:
                    merge = True
                    tags.pop(x)
                    tags.pop(x)
                    match = "%s %s" % (t1[0], t2[0])
                    pos = value
                    tags.insert(x, (match, pos))
                    break

        matches = []
        for t in tags:

            # If you only want a few tags,
            # use this one:
            if t[1] == "NNP" or t[1] == "NNI":
                matches.append(t[0])

            ## If you want a whole bunch of tags,
            ## use this one:
            #if t[1] == "NNP" or t[1] == "NNI" or t[1] == "NN":
            #    matches.append(t[0])

        return matches


def test():
    sentences = [
            "Results from automatically generated Jupyter Notebook and the researcher's observation and interpretation of results",
            "Identified differentially expressed genes and gene sets and small molecules predicted to reverse expression across all tissues",
            "Use the automatically generated Jupyter Notebook to observe and share results including common differentially expressed genes and gene sets that are unique for each tissue and identify common small molecules that are predicted to reverse expression across all tissues",
    ]
    for sentence in sentences:
        np_extractor = NouPhraseExtractor(sentence)
        result = np_extractor.extract()
        print("This sentence is about: %s" % ", ".join(result))

if __name__ == '__main__':
    test()


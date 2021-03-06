# The Verb in Biblical Hebrew 

## Most Recent Work

### 2017-10
**Timex and Verb Associations in Biblical Hebrew**
[`data_analysis/time_phrase_analysis.ipynb`](data_analysis/time_phrase_analysis.ipynb)


## Project Description
This repository contains jupyter notebooks related to my research on verbal tense/aspect in Biblical Hebrew. 

I am interested in approaching this question at the intersection between syntax and semantics—that is, the point at which formal structure and semantics coincide.

A lot of research has been generated on the question of the semantic role for the Biblical Hebrew verb. Little research, however, has approached the question from a computational perspective that keeps in view both questions of structure (position within clause, clause hierarchies, etc.) AND questions of semantics (classifications of words, the effect of combining certain word classes). Tense/Aspect research has to involve both levels: structural and semantic. 

Both syntactical and semantic approaches have weaknesses. Purely syntactical methods have two specific problems: 1) By treating semantics as secondary, these approaches do not address the semantic presuppositions that occur when they analyze their specimens. It is impossible to know that a given substantive is the subject of a verb of movement without knowing that it is a living entity (world knowledge). Or, to use a non-functional category, it is impossible to know the boundaries of a phrase(atom) or clause(atom) without knowing the semantic meaning of the words. This highlights a second weakness, that 2) purely syntactic approaches require human augmentation to identify sense units. In other words, a human operator tags elements as "Time" phrases, "Subj" phrases; or, a human identifies something as a participant in conversation with a computer script (as in ongoing research in participant tracking). Without these identifications, structural data is just numbers or grids on a screen—it means nothing on its own. Thus, while purely syntactic methods *require* semantics, they do not specify explicitly how semantic knowledge is derived.

Semantic methods fail to account for the importance of syntax in narrowing or extending the semantic range of a given term. Polysemy in language functions through the extension of terms through other elements in a clause. A term might mean "dog," a small furry mammal, on its own. But then it is used metaphorically in reference to a living human, "Bill...that dog!" where "there" refers backwards to "Bill" and identifies him as a "dog." In this case, the syntax is key! Other examples are the various meanings Hebrew verbs can assume with different prepositions (as in other languages). Limitations on the textual level, too, might limit or extend the sense. For instance, in a narrative which is based in a hospital, "doctor" has a different sense than the term as used in a story about a university (there could be a professor who walks into a hospital! But in that case, there would probably be an additional modifier for the person earlier in the narrative). Syntax and discourse structure cannot be ignored in establishing the semantic content of a word.

With the entire Hebrew Bible encoded syntactically in the `BHSA` (ETCBC) database, and with data processing tools like Python and R, these kinds of questions can be probed by computationally categorizing data based on its use, its occurrence within the clause/text, and subtle patterns encoded in the language itself.  

Here are a few initial research questions this entails:<br>
1. What kinds of syntactic structures can be used to generate word-relation ("semantic") data? (e.g. Snow, Jurafsky, Ng, ["Learning Syntactic Patterns for Automatic Hypernym Discovery"](http://ai.stanford.edu/~rion/papers/hypernym_nips05.pdf) or Hearst, ["Automatic Acquisition of Hyponyms from Large Text Corpora"](http://people.ischool.berkeley.edu/~hearst/papers/coling92.pdf))
1. What kinds of time markers occur alongside verb forms? (assumes a categorical classification of time indicators)
2. How does the distribution of verb forms within certain discourse structures affect the distribution of other verb forms?
3. [to be continued!]

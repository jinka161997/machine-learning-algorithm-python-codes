######### Text mining ################


######## Entity Recognizaiton #################
speech  = readLines("E:/Day Wise/Day 26 Text Mining Contd _ NLP/Data/modi.txt")
head(speech)

library(tm)
speech <- paste(speech, collapse = " ")
library(NLP)
library(openNLP)
library(magrittr)

speech <- as.String(speech)

word_ann <- Maxent_Word_Token_Annotator()
sent_ann <- Maxent_Sent_Token_Annotator()

speech_annotations <- annotate(speech, sent_ann)
head(speech_annotations)
?annotate
speech_doc <- AnnotatedPlainTextDocument(speech, speech_annotations)
sents(speech_doc) %>% head(5)

person_ann <- Maxent_Entity_Annotator(kind = "person")
location_ann <- Maxent_Entity_Annotator(kind = "location")
organization_ann <- Maxent_Entity_Annotator(kind = "organization")
?Maxent_Entity_Annotator
?annotate

annot.l1 = NLP::annotate(speech, list(sent_ann,
                                   word_ann,
                                   person_ann,
                                   location_ann,
                                   organization_ann))
k <- sapply(annot.l1$features, `[[`, "kind")
speech_persons = speech[annot.l1[k == "person"]]
speech_locations = speech[annot.l1[k == "location"]]
speech_organization = speech[annot.l1[k == "organization"]]

######### Emotion Mining ###############
library(syuzhet)
library(plotly)
library(tm)
s_v <- get_sentences(speech)

syuzhet <- get_sentiment(s_v, method="syuzhet")
bing <- get_sentiment(s_v, method="bing")
afinn <- get_sentiment(s_v, method="afinn")
nrc <- get_sentiment(s_v, method="nrc")
sentiments <- data.frame(syuzhet, bing, afinn, nrc)

#anger", "anticipation", "disgust", "fear", "joy", "sadness", 
#"surprise", "trust", "negative", "positive."
emotions <- get_nrc_sentiment(speech)
head(emotions)
emo_bar = colSums(emotions)
barplot(emo_bar)
emo_sum = data.frame(count=emo_bar, emotion=names(emo_bar))

plot(syuzhet, type = "l", main = "Plot Trajectory",
     xlab = "Narrative Time", ylab = "Emotional Valence")

# To extract the sentence with the most negative emotional valence
negative <- s_v[which.min(syuzhet)]

# and to extract the most positive sentence
positive <- s_v[which.max(syuzhet)]

############ Topic extraction ##################
library(tm)
library(slam)
library(topicmodels)

mydata.corpus <- Corpus(VectorSource(speech))
mydata.corpus <- tm_map(mydata.corpus, removePunctuation) 
my_stopwords <- c(stopwords('english'),"the", "due", "are", "not", "for", "this", "and",  "that", "there", "new", "near", "beyond","will","also","can", "time", 
                        "from", "been", "both", "than",  "has","now", "until", "all", "use", "two", "ave", "blvd", "east", "between", "end", "have", "avenue", "before",    "just", "mac", "being",  "when","levels","remaining","based", "still", "off", 
                    "over", "only", "north", "past", "twin", "while","then"
                    ,"Brothers","Sisters","sisters")
mydata.corpus <- tm_map(mydata.corpus, removeWords, my_stopwords)
mydata.corpus <- tm_map(mydata.corpus, removeNumbers) 

#Create document-term matrix
dtm <- DocumentTermMatrix(mydata.corpus)

#collapse matrix by summing over columns
freq <- colSums(as.matrix(dtm))
#length should be total number of terms
length(freq)
#create sort order (descending)
ord <- order(freq,decreasing=TRUE)
#List all terms in decreasing order of freq and write to disk
freq[ord]

library(NLP)
lda <- LDA(dtm, 10) # find 10 topics
term <- terms(lda, 5) # first 5 terms of every topic

#raw.sum=apply(dtm,1,FUN=sum) 
#dtm=dtm[raw.sum!=0,]

tops <- terms(lda)
tb <- table(names(tops), unlist(tops))
tb <- as.data.frame.matrix(tb)

cls <- hclust(dist(tb), method = 'ward.D2')
#par(family = "HiraKakuProN-W3")
plot(cls)

from pyspark.sql import SparkSession

# Crea una sessione Spark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Carica un file di testo
text_file = spark.read.text("test.txt")

# Esegui un conteggio di parole
word_count = text_file.selectExpr("explode(split(value, ' ')) as word").groupBy("word").count()

# Visualizza il risultato
word_count.show()

# Chiudi la sessione Spark
spark.stop()

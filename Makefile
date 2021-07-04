

all: mohanlal top_movies

top_movies:
	# "1980+"
	python3 scripts/get_movie_name_imdb.py https://www.imdb.com/list/ls008449472/ >> movie_names.tmp
	# "2010+"
	python3 scripts/get_movie_name_imdb.py https://www.imdb.com/list/ls087541655/ >> movie_names.tmp
	awk -F, '{print $1}' movie_names.tmp | awk '{if(NF<=2){print $0}}' | sort > movie_names.txt
	rm movie_names.tmp

mohanlal:
	python3 scripts/get_movie_name_wikipedia.py https://en.wikipedia.org/wiki/Mohanlal_filmography > character_names_mohanlal.txt

mammooty:
	python3 scripts/get_filmography_imdb.py https://www.imdb.com/name/nm0007123/

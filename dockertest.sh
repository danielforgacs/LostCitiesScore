docker run --rm -d -v $PWD:/home -e DEBUG=1 -p 8000:8000  --name testrun lostcitiesscore
docker run --rm -v $PWD:/home -e DEBUG=1 --network="host" lostcitiesscore pytest LostCitiesScore/
docker kill testrun
unamestr=$(uname)
echo $unamestr
if [ "$unamestr" = 'Linux' ]; then
  TODAY=`$expr date +"%d-%m-%y"`
  THIRTY_DAYS_AGO=`$expr date -d '-30 day' +"%d-%m-%y"`
elif [ "$unamestr" = 'Darwin' ]; then
  TODAY=`$expr gdate +"%d-%m-%y"`
  THIRTY_DAYS_AGO=`$expr gdate -d '-30 day' +"%d-%m-%y"`
fi

# dumping data to file
TODAYS_DB_FILE=dumps/db.sqlite3.backup_${TODAY}.json
echo "dumping data into $TODAYS_DB_FILE"
./manage.py dumpdata > $TODAYS_DB_FILE --settings=codingpro.settings.prod

# deleting old dumps
THIRTY_DAYS_AGO_DB_FILE=dumps/db.sqlite3.backup_${THIRTY_DAYS_AGO}.json
echo "deleting data file from 30 days ago $THIRTY_DAYS_AGO_DB_FILE"

if [ -f "$THIRTY_DAYS_AGO_DB_FILE" ]; then
  rm $THIRTY_DAYS_AGO_DB_FILE
  echo "file $THIRTY_DAYS_AGO_DB_FILE deleted"
else
  echo "file $THIRTY_DAYS_AGO_DB_FILE not found. Skipping"
fi


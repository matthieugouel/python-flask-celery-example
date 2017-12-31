if [ ! -z "$1" ]
then
    echo "Initialization of $1 project"
    ggrep -lri "api" | xargs gsed -i "s/api/$1/gI"
    mv api $1
    echo "Success ! You can now delete new.sh (rm new.sh)"
fi

pytest -v -s --browser chrome --html="HTMLReports\Bankapp_Chrome.html" -p no:warnings
pytest -v -s --browser edge --html="HTMLReports\Bankapp_Edge.html" -p no:warnings
pytest -v -s --browser firefox --html="HTMLReports\Bankapp_Firefox.html" -p no:warnings
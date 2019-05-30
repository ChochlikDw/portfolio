#!/usr/bin/env python3
import requests
import json
import pprint as pp


def get():
    nbp_url_a = "http://api.nbp.pl/api/exchangerates/tables/A?format=json"
    try:
        r = requests.get(nbp_url_a)
        data = r.json()
        with open("rates", 'w') as rates_file:
            json.dump(data, rates_file)
        msg = "Kursy aktualne z dn. {}.".format(data[0]["effectiveDate"])
    except:
        try:
            with open("rates", "r") as rates_file:
                data = json.load(rates_file)
        except:
            msg = "Brak dostępnych kursów. Brak dostępu do internetu oraz kopii offline."
        else:
            msg = "Kursy z dn. {}. ".format(data[0]["effectiveDate"]) + "Brak dostępu do internetu."
    rates = dict()
    try:
        for d in data[0]["rates"]:
            rates[d["code"]] = {"currency": d["currency"], "mid": d["mid"]}
    except:
        pass
    return rates, msg
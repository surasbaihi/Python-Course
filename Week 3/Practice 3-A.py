{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Available_Currencies_Dict: {'AED': 'United Arab Emirates Dirham', 'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'ANG': 'Netherlands Antillean Guilder', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'AWG': 'Aruban Florin', 'AZN': 'Azerbaijani Manat', 'BAM': 'Bosnia-Herzegovina Convertible Mark', 'BBD': 'Barbadian Dollar', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 'BMD': 'Bermudan Dollar', 'BND': 'Brunei Dollar', 'BOB': 'Bolivian Boliviano', 'BRL': 'Brazilian Real', 'BSD': 'Bahamian Dollar', 'BTC': 'Bitcoin', 'BTN': 'Bhutanese Ngultrum', 'BWP': 'Botswanan Pula', 'BYN': 'New Belarusian Ruble', 'BYR': 'Belarusian Ruble', 'BZD': 'Belize Dollar', 'CAD': 'Canadian Dollar', 'CDF': 'Congolese Franc', 'CHF': 'Swiss Franc', 'CLF': 'Chilean Unit of Account (UF)', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan', 'COP': 'Colombian Peso', 'CRC': 'Costa Rican Colón', 'CUC': 'Cuban Convertible Peso', 'CUP': 'Cuban Peso', 'CVE': 'Cape Verdean Escudo', 'CZK': 'Czech Republic Koruna', 'DJF': 'Djiboutian Franc', 'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EGP': 'Egyptian Pound', 'ERN': 'Eritrean Nakfa', 'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'FKP': 'Falkland Islands Pound', 'GBP': 'British Pound Sterling', 'GEL': 'Georgian Lari', 'GGP': 'Guernsey Pound', 'GHS': 'Ghanaian Cedi', 'GIP': 'Gibraltar Pound', 'GMD': 'Gambian Dalasi', 'GNF': 'Guinean Franc', 'GTQ': 'Guatemalan Quetzal', 'GYD': 'Guyanaese Dollar', 'HKD': 'Hong Kong Dollar', 'HNL': 'Honduran Lempira', 'HRK': 'Croatian Kuna', 'HTG': 'Haitian Gourde', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli New Sheqel', 'IMP': 'Manx pound', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 'IRR': 'Iranian Rial', 'ISK': 'Icelandic Króna', 'JEP': 'Jersey Pound', 'JMD': 'Jamaican Dollar', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling', 'KGS': 'Kyrgystani Som', 'KHR': 'Cambodian Riel', 'KMF': 'Comorian Franc', 'KPW': 'North Korean Won', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KYD': 'Cayman Islands Dollar', 'KZT': 'Kazakhstani Tenge', 'LAK': 'Laotian Kip', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'LRD': 'Liberian Dollar', 'LSL': 'Lesotho Loti', 'LTL': 'Lithuanian Litas', 'LVL': 'Latvian Lats', 'LYD': 'Libyan Dinar', 'MAD': 'Moroccan Dirham', 'MDL': 'Moldovan Leu', 'MGA': 'Malagasy Ariary', 'MKD': 'Macedonian Denar', 'MMK': 'Myanma Kyat', 'MNT': 'Mongolian Tugrik', 'MOP': 'Macanese Pataca', 'MRO': 'Mauritanian Ouguiya', 'MUR': 'Mauritian Rupee', 'MVR': 'Maldivian Rufiyaa', 'MWK': 'Malawian Kwacha', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'MZN': 'Mozambican Metical', 'NAD': 'Namibian Dollar', 'NGN': 'Nigerian Naira', 'NIO': 'Nicaraguan Córdoba', 'NOK': 'Norwegian Krone', 'NPR': 'Nepalese Rupee', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa', 'PEN': 'Peruvian Nuevo Sol', 'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar', 'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc', 'SAR': 'Saudi Riyal', 'SBD': 'Solomon Islands Dollar', 'SCR': 'Seychellois Rupee', 'SDG': 'Sudanese Pound', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 'SHP': 'Saint Helena Pound', 'SLL': 'Sierra Leonean Leone', 'SOS': 'Somali Shilling', 'SRD': 'Surinamese Dollar', 'STD': 'São Tomé and Príncipe Dobra', 'SVC': 'Salvadoran Colón', 'SYP': 'Syrian Pound', 'SZL': 'Swazi Lilangeni', 'THB': 'Thai Baht', 'TJS': 'Tajikistani Somoni', 'TMT': 'Turkmenistani Manat', 'TND': 'Tunisian Dinar', 'TOP': 'Tongan Paʻanga', 'TRY': 'Turkish Lira', 'TTD': 'Trinidad and Tobago Dollar', 'TWD': 'New Taiwan Dollar', 'TZS': 'Tanzanian Shilling', 'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'United States Dollar', 'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistan Som', 'VEF': 'Venezuelan Bolívar Fuerte', 'VND': 'Vietnamese Dong', 'VUV': 'Vanuatu Vatu', 'WST': 'Samoan Tala', 'XAF': 'CFA Franc BEAC', 'XAG': 'Silver (troy ounce)', 'XAU': 'Gold (troy ounce)', 'XCD': 'East Caribbean Dollar', 'XDR': 'Special Drawing Rights', 'XOF': 'CFA Franc BCEAO', 'XPF': 'CFP Franc', 'YER': 'Yemeni Rial', 'ZAR': 'South African Rand', 'ZMK': 'Zambian Kwacha (pre-2013)', 'ZMW': 'Zambian Kwacha', 'ZWL': 'Zimbabwean Dollar'}\n",
      "******************************\n",
      "Choose a currency you want to convert from :QAR\n",
      "******************************\n",
      "Available_Currencies_To_Dict : {'AED': 'United Arab Emirates Dirham', 'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'ANG': 'Netherlands Antillean Guilder', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'AWG': 'Aruban Florin', 'AZN': 'Azerbaijani Manat', 'BAM': 'Bosnia-Herzegovina Convertible Mark', 'BBD': 'Barbadian Dollar', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 'BMD': 'Bermudan Dollar', 'BND': 'Brunei Dollar', 'BOB': 'Bolivian Boliviano', 'BRL': 'Brazilian Real', 'BSD': 'Bahamian Dollar', 'BTC': 'Bitcoin', 'BTN': 'Bhutanese Ngultrum', 'BWP': 'Botswanan Pula', 'BYN': 'New Belarusian Ruble', 'BYR': 'Belarusian Ruble', 'BZD': 'Belize Dollar', 'CAD': 'Canadian Dollar', 'CDF': 'Congolese Franc', 'CHF': 'Swiss Franc', 'CLF': 'Chilean Unit of Account (UF)', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan', 'COP': 'Colombian Peso', 'CRC': 'Costa Rican Colón', 'CUC': 'Cuban Convertible Peso', 'CUP': 'Cuban Peso', 'CVE': 'Cape Verdean Escudo', 'CZK': 'Czech Republic Koruna', 'DJF': 'Djiboutian Franc', 'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EGP': 'Egyptian Pound', 'ERN': 'Eritrean Nakfa', 'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'FKP': 'Falkland Islands Pound', 'GBP': 'British Pound Sterling', 'GEL': 'Georgian Lari', 'GGP': 'Guernsey Pound', 'GHS': 'Ghanaian Cedi', 'GIP': 'Gibraltar Pound', 'GMD': 'Gambian Dalasi', 'GNF': 'Guinean Franc', 'GTQ': 'Guatemalan Quetzal', 'GYD': 'Guyanaese Dollar', 'HKD': 'Hong Kong Dollar', 'HNL': 'Honduran Lempira', 'HRK': 'Croatian Kuna', 'HTG': 'Haitian Gourde', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 'ILS': 'Israeli New Sheqel', 'IMP': 'Manx pound', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 'IRR': 'Iranian Rial', 'ISK': 'Icelandic Króna', 'JEP': 'Jersey Pound', 'JMD': 'Jamaican Dollar', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling', 'KGS': 'Kyrgystani Som', 'KHR': 'Cambodian Riel', 'KMF': 'Comorian Franc', 'KPW': 'North Korean Won', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KYD': 'Cayman Islands Dollar', 'KZT': 'Kazakhstani Tenge', 'LAK': 'Laotian Kip', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'LRD': 'Liberian Dollar', 'LSL': 'Lesotho Loti', 'LTL': 'Lithuanian Litas', 'LVL': 'Latvian Lats', 'LYD': 'Libyan Dinar', 'MAD': 'Moroccan Dirham', 'MDL': 'Moldovan Leu', 'MGA': 'Malagasy Ariary', 'MKD': 'Macedonian Denar', 'MMK': 'Myanma Kyat', 'MNT': 'Mongolian Tugrik', 'MOP': 'Macanese Pataca', 'MRO': 'Mauritanian Ouguiya', 'MUR': 'Mauritian Rupee', 'MVR': 'Maldivian Rufiyaa', 'MWK': 'Malawian Kwacha', 'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'MZN': 'Mozambican Metical', 'NAD': 'Namibian Dollar', 'NGN': 'Nigerian Naira', 'NIO': 'Nicaraguan Córdoba', 'NOK': 'Norwegian Krone', 'NPR': 'Nepalese Rupee', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa', 'PEN': 'Peruvian Nuevo Sol', 'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar', 'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc', 'SAR': 'Saudi Riyal', 'SBD': 'Solomon Islands Dollar', 'SCR': 'Seychellois Rupee', 'SDG': 'Sudanese Pound', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 'SHP': 'Saint Helena Pound', 'SLL': 'Sierra Leonean Leone', 'SOS': 'Somali Shilling', 'SRD': 'Surinamese Dollar', 'STD': 'São Tomé and Príncipe Dobra', 'SVC': 'Salvadoran Colón', 'SYP': 'Syrian Pound', 'SZL': 'Swazi Lilangeni', 'THB': 'Thai Baht', 'TJS': 'Tajikistani Somoni', 'TMT': 'Turkmenistani Manat', 'TND': 'Tunisian Dinar', 'TOP': 'Tongan Paʻanga', 'TRY': 'Turkish Lira', 'TTD': 'Trinidad and Tobago Dollar', 'TWD': 'New Taiwan Dollar', 'TZS': 'Tanzanian Shilling', 'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'United States Dollar', 'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistan Som', 'VEF': 'Venezuelan Bolívar Fuerte', 'VND': 'Vietnamese Dong', 'VUV': 'Vanuatu Vatu', 'WST': 'Samoan Tala', 'XAF': 'CFA Franc BEAC', 'XAG': 'Silver (troy ounce)', 'XAU': 'Gold (troy ounce)', 'XCD': 'East Caribbean Dollar', 'XDR': 'Special Drawing Rights', 'XOF': 'CFA Franc BCEAO', 'XPF': 'CFP Franc', 'YER': 'Yemeni Rial', 'ZAR': 'South African Rand', 'ZMK': 'Zambian Kwacha (pre-2013)', 'ZMW': 'Zambian Kwacha', 'ZWL': 'Zimbabwean Dollar'}\n",
      "******************************\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Choose a currency you want to convert to :CAD\n",
      "******************************\n",
      "Enter amount of money you want to convert :100\n",
      "100.0 QAR to CAD is 35.94715389291128\n"
     ]
    }
   ],
   "source": [
    "def Currency_Converter(from_curr ,to_curr ,amount):\n",
    "    \n",
    "    import requests\n",
    "    import json \n",
    "    import urllib.request\n",
    "    response = urllib.request.urlopen('http://data.fixer.io/api/symbols?access_key=f26f3c9bc66ed624bd6175175d4f812f')\n",
    "    Available_Currencies = response.read()\n",
    "\n",
    "    Available_Currencies_Dict = json.loads(Available_Currencies)\n",
    "    print(\"Available_Currencies_Dict:\" ,Available_Currencies_Dict[\"symbols\"])\n",
    "\n",
    "\n",
    "    print(\"******************************\")\n",
    "    \n",
    "    base_curr = input(\"Choose a currency you want to convert from :\")\n",
    "    \n",
    "\n",
    "    print(\"******************************\")\n",
    "    \n",
    "    print(\"Available_Currencies_To_Dict :\", Available_Currencies_Dict[\"symbols\"])\n",
    "    \n",
    "    \n",
    "    print(\"******************************\")\n",
    "    \n",
    "        \n",
    "    to_curr = input(\"Choose a currency you want to convert to :\")\n",
    "    \n",
    "    \n",
    "    print(\"******************************\")\n",
    "    \n",
    "\n",
    "    amount = float(input(\"Enter amount of money you want to convert :\"))\n",
    "\n",
    "    import requests   \n",
    "    base_link_forex = 'http://data.fixer.io/api/latest'\n",
    "    parameters_forex = {\n",
    "        \"access_key\":\"e1be8ec55a7c5fa9600ff656adf94ac4\",\n",
    "        \"from\" : \"base_curr\",\n",
    "        \"to\" : \"to_curr\",\n",
    "        \"amount\" : amount \n",
    "    }\n",
    "    \n",
    "    response = requests.get(base_link_forex,parameters_forex).json()\n",
    "\n",
    "    latest_Euro_rates = {\n",
    "\n",
    "       \"AED\": float(response[\"rates\"][\"AED\"]),\n",
    "       \"AFN\": float(response[\"rates\"][\"AFN\"]),\n",
    "       \"ALL\": float(response[\"rates\"][\"ALL\"]),\n",
    "       \"AMD\": float(response[\"rates\"][\"AMD\"]),\n",
    "       \"ANG\": float(response[\"rates\"][\"ANG\"]),\n",
    "       \"AOA\": float(response[\"rates\"][\"AOA\"]),\n",
    "       \"ARS\": float(response[\"rates\"][\"ARS\"]),\n",
    "       \"AUD\": float(response[\"rates\"][\"AUD\"]),\n",
    "       \"AWG\": float(response[\"rates\"][\"AWG\"]),\n",
    "       \"AZN\": float(response[\"rates\"][\"AZN\"]),\n",
    "       \"BAM\": float(response[\"rates\"][\"BAM\"]),\n",
    "       \"BBD\": float(response[\"rates\"][\"BBD\"]),\n",
    "       \"BDT\": float(response[\"rates\"][\"BDT\"]),\n",
    "       \"BGN\": float(response[\"rates\"][\"BGN\"]),\n",
    "       \"BHD\": float(response[\"rates\"][\"BHD\"]),\n",
    "       \"BIF\": float(response[\"rates\"][\"BIF\"]),\n",
    "       \"BMD\": float(response[\"rates\"][\"BMD\"]),\n",
    "       \"BND\": float(response[\"rates\"][\"BND\"]),\n",
    "       \"BOB\": float(response[\"rates\"][\"BOB\"]),\n",
    "       \"BRL\": float(response[\"rates\"][\"BRL\"]),\n",
    "       \"BSD\": float(response[\"rates\"][\"BSD\"]),\n",
    "       \"BTC\": float(response[\"rates\"][\"BTC\"]),\n",
    "       \"BTN\": float(response[\"rates\"][\"BTN\"]),\n",
    "       \"BWP\": float(response[\"rates\"][\"BWP\"]),\n",
    "       \"BYR\": float(response[\"rates\"][\"BYR\"]),\n",
    "       \"BYN\": float(response[\"rates\"][\"BYN\"]),\n",
    "       \"BZD\": float(response[\"rates\"][\"BZD\"]),\n",
    "       \"CAD\": float(response[\"rates\"][\"CAD\"]),\n",
    "       \"CDF\": float(response[\"rates\"][\"CDF\"]),\n",
    "       \"CHF\": float(response[\"rates\"][\"CHF\"]),\n",
    "       \"CLF\": float(response[\"rates\"][\"CLF\"]),\n",
    "       \"CLP\": float(response[\"rates\"][\"CLP\"]),\n",
    "       \"CNY\": float(response[\"rates\"][\"CNY\"]),\n",
    "       \"COP\": float(response[\"rates\"][\"COP\"]),\n",
    "       \"CRC\": float(response[\"rates\"][\"CRC\"]),\n",
    "       \"CUC\": float(response[\"rates\"][\"CUC\"]),\n",
    "       \"CUP\": float(response[\"rates\"][\"CUP\"]),\n",
    "       \"CVE\": float(response[\"rates\"][\"CVE\"]),\n",
    "       \"CZK\": float(response[\"rates\"][\"CZK\"]),\n",
    "       \"DJF\": float(response[\"rates\"][\"DJF\"]),\n",
    "       \"DKK\": float(response[\"rates\"][\"DKK\"]),\n",
    "       \"DOP\": float(response[\"rates\"][\"DOP\"]),\n",
    "       \"DZD\": float(response[\"rates\"][\"DZD\"]),\n",
    "       \"EGP\": float(response[\"rates\"][\"EGP\"]),\n",
    "       \"ERN\": float(response[\"rates\"][\"ERN\"]),\n",
    "       \"ETB\": float(response[\"rates\"][\"ETB\"]),\n",
    "       \"EUR\": float(response[\"rates\"][\"EUR\"]),\n",
    "       \"FJD\": float(response[\"rates\"][\"FJD\"]),\n",
    "       \"FKP\": float(response[\"rates\"][\"FKP\"]),\n",
    "       \"GBP\": float(response[\"rates\"][\"GBP\"]),\n",
    "       \"GEL\": float(response[\"rates\"][\"GEL\"]),\n",
    "       \"GGP\": float(response[\"rates\"][\"GGP\"]),\n",
    "       \"GHS\": float(response[\"rates\"][\"GHS\"]),\n",
    "       \"GIP\": float(response[\"rates\"][\"GIP\"]),\n",
    "       \"GMD\": float(response[\"rates\"][\"GMD\"]),\n",
    "       \"GNF\": float(response[\"rates\"][\"GNF\"]),\n",
    "       \"GTQ\": float(response[\"rates\"][\"GTQ\"]),\n",
    "       \"GYD\": float(response[\"rates\"][\"GYD\"]),\n",
    "       \"HKD\": float(response[\"rates\"][\"HKD\"]),\n",
    "       \"HNL\": float(response[\"rates\"][\"HNL\"]),\n",
    "       \"HRK\": float(response[\"rates\"][\"HRK\"]),\n",
    "       \"HTG\": float(response[\"rates\"][\"HTG\"]),\n",
    "       \"HUF\": float(response[\"rates\"][\"HUF\"]),\n",
    "       \"IDR\": float(response[\"rates\"][\"IDR\"]),\n",
    "       \"ILS\": float(response[\"rates\"][\"ILS\"]),\n",
    "       \"IMP\": float(response[\"rates\"][\"IMP\"]),\n",
    "       \"INR\": float(response[\"rates\"][\"INR\"]),\n",
    "       \"IQD\": float(response[\"rates\"][\"IQD\"]),\n",
    "       \"IRR\": float(response[\"rates\"][\"IRR\"]),\n",
    "       \"ISK\": float(response[\"rates\"][\"ISK\"]),\n",
    "       \"JEP\": float(response[\"rates\"][\"JEP\"]),\n",
    "       \"JMD\": float(response[\"rates\"][\"JMD\"]),\n",
    "       \"JOD\": float(response[\"rates\"][\"JOD\"]),\n",
    "       \"JPY\": float(response[\"rates\"][\"JPY\"]),\n",
    "       \"KES\": float(response[\"rates\"][\"KES\"]),\n",
    "       \"KGS\": float(response[\"rates\"][\"KGS\"]),\n",
    "       \"KHR\": float(response[\"rates\"][\"KHR\"]),\n",
    "       \"KMF\": float(response[\"rates\"][\"KMF\"]),\n",
    "       \"KPW\": float(response[\"rates\"][\"KPW\"]),\n",
    "       \"KRW\": float(response[\"rates\"][\"KRW\"]),\n",
    "       \"KWD\": float(response[\"rates\"][\"KWD\"]),\n",
    "       \"KYD\": float(response[\"rates\"][\"KYD\"]),\n",
    "       \"KZT\": float(response[\"rates\"][\"KZT\"]),\n",
    "       \"LAK\": float(response[\"rates\"][\"LAK\"]),\n",
    "       \"LBP\": float(response[\"rates\"][\"LBP\"]),\n",
    "       \"LKR\": float(response[\"rates\"][\"LKR\"]),\n",
    "       \"LRD\": float(response[\"rates\"][\"LRD\"]),\n",
    "       \"LSL\": float(response[\"rates\"][\"LSL\"]),\n",
    "       \"LTL\": float(response[\"rates\"][\"LTL\"]),\n",
    "       \"LVL\": float(response[\"rates\"][\"LVL\"]),\n",
    "       \"LYD\": float(response[\"rates\"][\"LYD\"]),\n",
    "       \"MAD\": float(response[\"rates\"][\"MAD\"]),\n",
    "       \"MDL\": float(response[\"rates\"][\"MDL\"]),\n",
    "       \"MGA\": float(response[\"rates\"][\"MGA\"]),\n",
    "       \"MKD\": float(response[\"rates\"][\"MKD\"]),\n",
    "       \"MMK\": float(response[\"rates\"][\"MMK\"]),\n",
    "       \"MNT\": float(response[\"rates\"][\"MNT\"]),\n",
    "       \"MOP\": float(response[\"rates\"][\"MOP\"]),\n",
    "       \"MRO\": float(response[\"rates\"][\"MRO\"]),\n",
    "       \"MUR\": float(response[\"rates\"][\"MUR\"]),\n",
    "       \"MVR\": float(response[\"rates\"][\"MVR\"]),\n",
    "       \"MWK\": float(response[\"rates\"][\"MWK\"]),\n",
    "       \"MXN\": float(response[\"rates\"][\"MXN\"]),\n",
    "       \"MYR\": float(response[\"rates\"][\"MYR\"]),\n",
    "       \"MZN\": float(response[\"rates\"][\"MZN\"]),\n",
    "       \"NAD\": float(response[\"rates\"][\"NAD\"]),\n",
    "       \"NGN\": float(response[\"rates\"][\"NGN\"]),\n",
    "       \"NIO\": float(response[\"rates\"][\"NIO\"]),\n",
    "       \"NOK\": float(response[\"rates\"][\"NOK\"]),\n",
    "       \"NPR\": float(response[\"rates\"][\"NPR\"]),\n",
    "       \"NZD\": float(response[\"rates\"][\"NZD\"]),\n",
    "       \"OMR\": float(response[\"rates\"][\"OMR\"]),\n",
    "       \"PAB\": float(response[\"rates\"][\"PAB\"]),\n",
    "       \"PEN\": float(response[\"rates\"][\"PEN\"]),\n",
    "       \"PGK\": float(response[\"rates\"][\"PGK\"]),\n",
    "       \"PHP\": float(response[\"rates\"][\"PHP\"]),\n",
    "       \"PKR\": float(response[\"rates\"][\"PKR\"]),\n",
    "       \"PLN\": float(response[\"rates\"][\"PLN\"]),\n",
    "       \"PYG\": float(response[\"rates\"][\"PYG\"]),\n",
    "       \"QAR\": float(response[\"rates\"][\"QAR\"]),\n",
    "       \"RON\": float(response[\"rates\"][\"RON\"]),\n",
    "       \"RSD\": float(response[\"rates\"][\"RSD\"]),\n",
    "       \"RUB\": float(response[\"rates\"][\"RUB\"]),\n",
    "       \"RWF\": float(response[\"rates\"][\"RWF\"]),\n",
    "       \"SAR\": float(response[\"rates\"][\"SAR\"]),\n",
    "       \"SBD\": float(response[\"rates\"][\"SBD\"]),\n",
    "       \"SCR\": float(response[\"rates\"][\"SCR\"]),\n",
    "       \"SDG\": float(response[\"rates\"][\"SDG\"]),\n",
    "       \"SEK\": float(response[\"rates\"][\"SEK\"]),\n",
    "       \"SGD\": float(response[\"rates\"][\"SGD\"]),\n",
    "       \"SHP\": float(response[\"rates\"][\"SHP\"]),\n",
    "       \"SLL\": float(response[\"rates\"][\"SLL\"]),\n",
    "       \"SOS\": float(response[\"rates\"][\"SOS\"]),\n",
    "       \"SRD\": float(response[\"rates\"][\"SRD\"]),\n",
    "       \"STD\": float(response[\"rates\"][\"STD\"]),\n",
    "       \"SVC\": float(response[\"rates\"][\"SVC\"]),\n",
    "       \"SYP\": float(response[\"rates\"][\"SYP\"]),\n",
    "       \"SZL\": float(response[\"rates\"][\"SZL\"]),\n",
    "       \"THB\": float(response[\"rates\"][\"THB\"]),\n",
    "       \"TJS\": float(response[\"rates\"][\"TJS\"]),\n",
    "       \"TMT\": float(response[\"rates\"][\"TMT\"]),\n",
    "       \"TND\": float(response[\"rates\"][\"TND\"]),\n",
    "       \"TOP\": float(response[\"rates\"][\"TOP\"]),\n",
    "       \"TRY\": float(response[\"rates\"][\"TRY\"]),\n",
    "       \"TTD\": float(response[\"rates\"][\"TTD\"]),\n",
    "       \"TWD\": float(response[\"rates\"][\"TWD\"]),\n",
    "       \"TZS\": float(response[\"rates\"][\"TZS\"]),\n",
    "       \"UAH\": float(response[\"rates\"][\"UAH\"]),\n",
    "       \"UGX\": float(response[\"rates\"][\"UGX\"]),\n",
    "       \"USD\": float(response[\"rates\"][\"USD\"]),\n",
    "       \"UYU\": float(response[\"rates\"][\"UYU\"]),\n",
    "       \"UZS\": float(response[\"rates\"][\"UZS\"]),\n",
    "       \"VEF\": float(response[\"rates\"][\"VEF\"]),\n",
    "       \"VND\": float(response[\"rates\"][\"VND\"]),\n",
    "       \"VUV\": float(response[\"rates\"][\"VUV\"]),\n",
    "       \"WST\": float(response[\"rates\"][\"WST\"]),\n",
    "       \"XAF\": float(response[\"rates\"][\"XAF\"]),\n",
    "       \"XAG\": float(response[\"rates\"][\"XAG\"]),\n",
    "       \"XAU\": float(response[\"rates\"][\"XAU\"]),\n",
    "       \"XCD\": float(response[\"rates\"][\"XCD\"]),\n",
    "       \"XDR\": float(response[\"rates\"][\"XDR\"]),\n",
    "       \"XOF\": float(response[\"rates\"][\"XOF\"]),\n",
    "       \"XPF\": float(response[\"rates\"][\"XPF\"]),\n",
    "       \"YER\": float(response[\"rates\"][\"YER\"]),\n",
    "       \"ZAR\": float(response[\"rates\"][\"ZAR\"]),\n",
    "       \"ZMK\": float(response[\"rates\"][\"ZMK\"]),\n",
    "       \"ZMW\": float(response[\"rates\"][\"ZMW\"]),\n",
    "       \"ZWL\": float(response[\"rates\"][\"ZWL\"]),\n",
    "    }\n",
    "    Result = (latest_Euro_rates[to_curr]/latest_Euro_rates[base_curr]) * amount\n",
    "    print(f\"{amount} {base_curr} to {to_curr} is {Result}\")\n",
    "Currency_Converter(\"USD\",\"JOR\",1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
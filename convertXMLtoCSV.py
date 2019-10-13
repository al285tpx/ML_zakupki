from xml.dom import minidom
import xml.etree.ElementTree as ET
import csv


xml_data_to_csv = open('tenderPlan_44201603621000114001_13856628.csv', 'w')

list_head = ['positionNumber', 'code', 'year', 'yearAmount', 'code2', 'name', 'contractSubjectName', 'contractMaxPrice', 'payments', 'codeCurrency', 'nameCurrency', 'codePlacingWay', 'namePlacingWay', 'features111', 'positionPublishDate']

csvWriter = csv.writer(xml_data_to_csv)
csvWriter.writerow(list_head)

xmldoc = minidom.parse("tenderPlan_44201603621000114001_13856628.xml")
export = xmldoc.getElementsByTagName("ns2:export")[0]
tenderPlan = export.getElementsByTagName("ns2:tenderPlan")[0]
providedPurchases = tenderPlan.getElementsByTagName("providedPurchases")[0]
positionss = providedPurchases.getElementsByTagName("positions")[0]
position = positionss.getElementsByTagName("position")

for positions in position:
    try:
        list_nodes = []
        positionNumber = positions.getElementsByTagName("positionNumber")[0].firstChild.data
        list_nodes.append(positionNumber)
        amountKBKs2016Years = positions.getElementsByTagName("amountKBKs2016Years")[0]
        KBK2016 = amountKBKs2016Years.getElementsByTagName("KBK2016")[0]
        code = KBK2016.getElementsByTagName("code")[0].firstChild.data
        list_nodes.append(code)
        yearsList = KBK2016.getElementsByTagName("yearsList")[0]
        year = yearsList.getElementsByTagName("year")[0].firstChild.data
        list_nodes.append(year)
        yearAmount = yearsList.getElementsByTagName("yearAmount")[0].firstChild.data
        list_nodes.append(yearAmount)
        OKVEDs = positions.getElementsByTagName("OKVEDs")[0]
        OKVED2 = OKVEDs.getElementsByTagName("OKVED2")[0]
        code2 = OKVED2.getElementsByTagName("code")[0].firstChild.data
        list_nodes.append(code2)
        name = OKVED2.getElementsByTagName("name")[0].firstChild.data
        list_nodes.append(name)
        contractSubjectName = positions.getElementsByTagName("contractSubjectName")[0].firstChild.data
        list_nodes.append(contractSubjectName)
        contractMaxPrice = positions.getElementsByTagName("contractMaxPrice")[0].firstChild.data
        list_nodes.append(contractMaxPrice)
        payments = positions.getElementsByTagName("payments")[0].firstChild.data
        list_nodes.append(payments)
        contractCurrency = positions.getElementsByTagName("contractCurrency")[0]
        codeCurrency = contractCurrency.getElementsByTagName("code")[0].firstChild.data
        list_nodes.append(codeCurrency)
        nameCurrency = contractCurrency.getElementsByTagName("name")[0].firstChild.data
        list_nodes.append(nameCurrency)
        placingWay = positions.getElementsByTagName("placingWay")[0]
        codePlacingWay = placingWay.getElementsByTagName("code")[0].firstChild.data
        list_nodes.append(codePlacingWay)
        namePlacingWay = placingWay.getElementsByTagName("name")[0].firstChild.data
        list_nodes.append(namePlacingWay)
        features111 = positions.getElementsByTagName("features111")[0].firstChild.data
        list_nodes.append(features111)
        positionPublishDate = positions.getElementsByTagName("positionPublishDate")[0].firstChild.data
        list_nodes.append(positionPublishDate)
    except IndexError:
        pass

    csvWriter.writerow(list_nodes)

xml_data_to_csv.close()


   # print(positionNumber+"," , code+",", year+",", yearAmount+",", code2+",", name)
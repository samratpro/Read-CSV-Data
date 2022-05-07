import csv

#Start CSV File reading
with open('product.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    dicts = {}
    i = 0
    for list in csv_reader:
        dicts[i] = {
            'keyword':list[0],
            'p1-lnk':list[1],
            'p1-fe':list[2],
            'info-1': list[21],
            'info-2': list[22],
            'buy-1': list[26],
            'buy-2': list[27]
        }
        i = i + 1
csv_file.close()
#End CSV File reading


post_run = 1
while post_run < len(dicts):
  #Link, Image, Title, Info, buying
  p1lnk = dicts[post_run]['p1-lnk']
  p1fe = dicts[post_run]['p1-fe']
  info1 = dicts[post_run]['info-1']
  info2 = dicts[post_run]['info-2']
  buy1 = dicts[post_run]['buy-1']
  buy2 = dicts[post_run]['buy-2']
  
  print(p1lnk)
  print(p1fe)
  print(info1)
  print(info2)
  print(buy1)
  print(buy2)

  post_run += 1

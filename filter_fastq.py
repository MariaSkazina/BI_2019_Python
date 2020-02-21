import argparse, gzip, os

parser = argparse.ArgumentParser(description="Фильтрация fastq файлов")

parser.add_argument("--min_length", help="Минимальная длина рида, по умолчанию 30 п.н.", required = True, default = "30", type=int)
parser.add_argument("--keep_filtered", help="Если указан этот флаг, то отбракованные риды запишутся в отдельный файл")
parser.add_argument("--gc_bounds_up", "--gc_bounds_down", help="Доля GC оснований в риде")
#parser.add_argument("--gc_bounds_up", help="Доля GC оснований в риде")
parser.add_argument("-o", "--output", help="Начало названия файлов с результатом фильтрации", default="stdout")
parser.add_argument("input", help="Название файла с прочтениями", default="stdin")

args = parser.parse_args()
#проверка расширения
extension = os.path.splitext(args.input)
infile = sys.stdin
if extension == ".fastq":
    pass
if extension == ".gz":
    infile = gzip.open(args.input, "rb")
else:
    sys.exit("Неизвестный формат файла")

lines_in_read = 4

for lines in infile:
    if len(line) < 30:
        pass

with open(output,'w'):
    min_len = sys.min_length
    c = 0
    for line in infile:
        line = line.rstrip()
        if line.startswith('>') and len(line)>30:
        if len(line) > 30:
            res = {}
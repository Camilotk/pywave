from composer import notes, timing
import wavepacker as wp

sheet = [
    (notes["A"], 4000),
]

sheet = wp.notes_packer(sheet)
# print(sheet)
wp.pack(sheet, "tinkle")
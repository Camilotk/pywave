from composer import notes, timing
import signalgenerator as sg
import wavepacker as wp

risen_sheet = [
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['half']),
    (notes['C#'], timing['whole']),
    (notes['A#'], timing['whole']),
    (notes['A#'], timing['whole']),
    (notes['A#'], timing['half']),
    (notes['A#'], timing['half']),
    (notes['A#'], timing['half']),
    (notes['A#'], timing['half']),
    (notes['G'], timing['half']),
    (notes['G'], timing['half']),
    (notes['G'], timing['half']),
    (notes['G'], timing['half']),
    (notes['G'], timing['whole']),
    (notes['G'], timing['whole']),
    (notes['A#'], timing['whole']),
    (notes['A#'], timing['half']),
    (notes['A#'], timing['half']),
    (notes['A#'], timing['half']),
    (notes['A#'], timing['half']),
    (notes['A#'], timing['whole']),
    # ...
]



sheet = wp.notes_packer(risen_sheet)
# print(sheet)
wp.pack(sheet, "risen")
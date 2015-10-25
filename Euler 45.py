def find():
    tri_step = 285
    pent_step = 165
    hex_step = 143

    tri = 40755
    pent = 40755
    hex = 40755

    def gen_tri(step):
        return step * (step + 1) / 2

    def gen_pent(step):
        return step * (3 * step - 1) / 2

    def gen_hex(step):
        return step * (2 * step - 1)

    hex_step += 1
    hex = gen_hex(hex_step)
    while hex != pent and hex != tri:
        while pent < hex:
            pent_step += 1
            pent = gen_pent(pent_step)
        if pent == hex:
            while tri < pent:
                tri_step += 1
                tri = gen_tri(tri_step)

            if tri == pent: return tri
        hex_step += 1
        hex = gen_hex(hex_step)


print(find())

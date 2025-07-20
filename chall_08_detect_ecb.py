from set_01_utils import hex_to_bytes, hamming_distance, bytes_to_hex, ecb_decrypt

if __name__ == "__main__":
    min_score = (-1, b'')
    with open("chall_08_input.txt") as file:
        for line in file:
            bytes_line = hex_to_bytes(line.strip())
            blocks = [bytes_line[i : i + 8] for i in range(0, len(bytes_line), 8)]
            if len(blocks[-1]) != 8:
                continue
            curr_score = 0
            for i in range(len(blocks)):
                for j in range(i + 1, len(blocks)):
                    curr_score += hamming_distance(blocks[i], blocks[j])
            curr_score /= len(blocks) * (len(blocks) - 1) # to compute average, n*(n-1) entries 
            if min_score[0] == -1 or min_score[0] > curr_score:
                min_score = (curr_score, bytes_line)
    print((min_score[0], bytes_to_hex(min_score[1])))

import sys

class SuffixArray:
    def __init__(self, text: str):
        self.text = text.lower() + "$"
        self.suffix_array = self.build_suffix_array()

    def build_suffix_array(self):
        n = len(self.text)

        suffixes = list(range(n))

        sorted_char = sorted(set(self.text))
        char_rank = {c: i for i, c in enumerate(sorted_char)}
        rank = [char_rank[c] for c in self.text]

        step = 1
        while step < n:
            suffixes = sorted(suffixes, key=lambda i: (rank[i], rank[i + step] if i + step < n else -1))

            new_rank = [0] * n
            for i in range(1, n):
                prev, curr = suffixes[i - 1], suffixes[i]

                if (rank[prev], rank[prev + step] if prev + step < n else -1) != \
                   (rank[curr], rank[curr + step] if curr + step < n else -1):
                    new_rank[curr] = new_rank[prev] + 1
                else:
                    new_rank[curr] = new_rank[prev]

            rank = new_rank
            step *= 2
        return suffixes


def search_query_position(full_text: str, suffix_array: list, query: str) -> list:
    full_text = full_text
    query = query.lower()
    n = len(suffix_array)


    def lower_bound():
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            suffix = full_text[suffix_array[mid]:]
            # Compara lexicográficamente el prefijo del sufijo con la query
            if suffix[:len(query)] < query:
                left = mid + 1
            else:
                right = mid
        return left


    def upper_bound():
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            suffix = full_text[suffix_array[mid]:]
            if suffix[:len(query)] <= query:
                left = mid + 1
            else:
                right = mid
        return left

    start = lower_bound()
    end = upper_bound()

    return sorted(suffix_array[start:end] if start < end else [])

def main():
    if len(sys.argv) < 3:
        print("Usage: python suffix_array_search.py <input_file> <query_file> [<output_file>]")
        sys.exit(1)

    input_file = sys.argv[1]
    query_file = sys.argv[2]


    if len(sys.argv) > 3:
        output_file = sys.argv[3]
        out_f = open(output_file, "w", encoding="utf-8")
    else:
        out_f = sys.stdout

    # 1. Read input file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
        print("File read successfully")

    # 2. Build suffix array
    suffix_array_obj = SuffixArray(text)
    sa = suffix_array_obj.suffix_array

    # 3. Read query file
    with open(query_file, "r", encoding="utf-8") as f:
        queries = [line.strip() for line in f if line.strip()]
        print("Query file read successfully")

    # 4. Search query positions
    for query in queries:
        print(f"Searching positions for query: {query}")
        positions = search_query_position(suffix_array_obj.text, sa, query)

        out_f.write(query + "\t" + "\t".join(map(str, positions)) + "\n")

    out_f.close()

if __name__ == "__main__":
    main()






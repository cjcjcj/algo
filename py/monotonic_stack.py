def increasing(ns: list):
    """
        nearest smaller element
    """
    st = []
    for n in ns:
        while st and st[-1] > n:
            st.pop()
        st.append(n)

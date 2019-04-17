(defun palindrome (l)
    (equal l (reverse l)))

(print(palindrome '(a b c )))
(print(palindrome '(m a d a m)))
(print(palindrome '(cat dog)))
(print(palindrome '()))
(print(palindrome '(cat dog bird bird dog cat)))

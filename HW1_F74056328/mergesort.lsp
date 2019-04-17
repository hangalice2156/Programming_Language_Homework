(defun single (sequence)
    (if (consp sequence)
        (not (cdr sequence))
        (= (length sequence) 1)
    )
)


(defun mergesort (numbers)
    (if (or (null numbers) (single numbers))
        (return-from mergesort numbers)
        (let ((half (truncate (/ (length numbers) 2))))
            (merge (type-of numbers)
                (mergesort (subseq numbers 0 half))
                (mergesort (subseq numbers half))
                #'<)
        )
    )
)

; main function
(let ((n (read)) (numbers))
    (setf numbers
        (do 
            ((i 0 (+ i 1)) (tmp nil)) 
            ((>= i n) (reverse tmp))
            (setf tmp (cons (read) tmp))
        )
    )
    (format t "~{~A ~}~%" (mergesort numbers))
)

;(print (mergesort '(4 5 3 9 1))) ;for debug usage
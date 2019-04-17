(print "The default value for fib1 and fib2 is 6.")

(defun fib1 (n)
    (IF (< n 2)
        n
        (+ (fib1 (- n 1)) (fib1 (- n 2)))
    )
)
(trace fib1)
(print (fib1 6))

(defun fib2 (n a b)
    (if (= n 0)
        a
        (fib2 (- n 1) b (+ a b))
    )
)

(trace fib2)
(print (fib2 6 0 1))

;;(defun fib (n)
;;    (labels ((calc-fib (n a b)
;;        (if (= n 0)
;;            a
;;            (calc-fib (- n 1) b (+ a b)))))
;;        (calc-fib n 0 1)
;;    )
;;)

;;(trace fib)
;;(print (fib 6))
;;the trace function will not trace the things inside the labels
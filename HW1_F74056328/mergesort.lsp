(defun mergesort (numbers)
    (return-from mergesort numbers))
; main function

(let ((n (read)) (numbers))
    (setf numbers
        (do ((i 0 (+ i 1)) (tmp nil)) ((>= i n) (reverse tmp))
            (setf tmp (cons (read) tmp))))
(format t "~{~A ~}~%" (mergesort numbers)))
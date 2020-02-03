
(cl:in-package :asdf)

(defsystem "joystick-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "JoyStick" :depends-on ("_package_JoyStick"))
    (:file "_package_JoyStick" :depends-on ("_package"))
  ))
class Characters:
    __original = 'abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ0123456789,.<>:;\\/\'' \
                 '?|"~^]}[-_=+àáâãèéêêíìĩîóòõôúùũûÁÀÃÂÉÈẼÊÍÌĨÎÓÒÕÔÚÙŨÛ!@#$%*() ¹²³£¢¬{[]§ªº°\n'
    __scrambled = '7@A_Û(Înũdi[Ì{Â2vjâ\nìàúPÒ^LN.IG=T²3qhoe6< $Yafò*áêm\\À+]Ùí;1pZÈHº£zXW9Ũ?' \
                  ',!¢-ùèEw4~uÁêéî¹Ó}§]#¬VÔsã5³ôlbÊÍDÉFKS\'ĩx:%rªõ°Ã/8Õ[>RkOMUẼ|)ĨcyBÚûJtgó"0CQ'

    @property
    def original(self) -> [str]:
        return list(self.__original)

    @property
    def scrambled(self) -> [str]:
        return list(self.__scrambled)
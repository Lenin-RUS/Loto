from game import meshok, card, user


class TestMeshok:

    def test_meshok_init(self):
        new_bag=meshok()
        assert new_bag.current_barrel==0
        assert len(new_bag.numbers)==90

    def test_meshok_get_barrel(self):
        new_bag=meshok()
        new_bag.get_barrel(5)
        assert new_bag.current_barrel in new_bag.numbers

class TestCard:

    def test_card_init(self):
        tmp_player='Иван'
        new_card=card(tmp_player)
        assert len(new_card.numbers)==27
        assert new_card.state == 1
        assert new_card.user == tmp_player

    def test_show_card(self):
        tmp_player='Иван'
        new_card=card(tmp_player)
        assert new_card.show_card()==1

    def test_check_number(self):
        new_bag=meshok()
        tmp_player_name='Иван'
        new_card=card(tmp_player_name)
        tmp_player=user(tmp_player_name, 1)
        for i in new_bag.numbers:
            new_card.check_number(i, tmp_player)
        # должны получиться одни 0
        assert sum(new_card.numbers)==0

class TestUser:
    def test_user_init(self):
        tmp_player_name='Иван'
        tmp_player=user(tmp_player_name, 1)
        assert tmp_player.name==tmp_player_name
        assert tmp_player.player_status == 1
        assert tmp_player.player_type == 1
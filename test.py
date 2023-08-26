import pytest
from bonus import bonus_calculation


@pytest.mark.parametrize('er', [("26/08/2020", 28),  # 3 years
                                ("05/08/2017", 33),  # more than 3 years
                                ("26/06/2021", 28),  # 2 years
                                ("26/03/2022", 18),  # 1.5 years
                                ("16/02/2022", 28),  # 1.6 years
                                ("28/05/2023", 18),  # 90 days
                                ("26/05/2023", 18),  # 92 days
                                ("19/08/2023", 0),  # 7 days
                                ("26/08/2023", 0),  # today's date
                                ("15/07/2022", 18)])  # less than 1.5 years
def test_bonus_based_on_working_years(er):
    assert bonus_calculation(er[0]) == er[1], "bonus calculation is incorrect!"


@pytest.mark.parametrize('er', [("05/08/2017", "26/03/2023", 30),  # more than 3 years and sick leave
                                ("26/06/2021", "26/04/2023", 25),  # 2 years and sick leave
                                ("26/03/2022", "26/04/2023", 15),  # 1.5 years
                                ("16/02/2022", "26/04/2022", 28)  # 1.6 years and last year sick leave
                                ])
def test_bonus_based_on_working_years_and_sick_leave(er):
    assert bonus_calculation(er[0], er[1]) == er[2], "bonus calculation is incorrect!"


@pytest.mark.parametrize('er', [("28/05/2023", "26/04/2022", "Date of sick leave cannot be before the hiring date!"),
                                # 90 days and sick leave prior the employment
                                ("26/05/2023", "26/04/2024", "Date of sick leave cannot be in the future!"),
                                # 92 days and sick leave in future
                                ("19.08.23", "26/04/2022", "Please correct the data, it should be in format %d/%m/%Y"),
                                # incorrect data format
                                ("26/04/2021", 4, "Please correct the data, it should be in format %d/%m/%Y"),
                                # incorrect data format
                                ("15/07/2024", "26/08/2024", "The person hasn't been hired yet!")
                                # date of employment in the future
                                ])
def test_exceptions(er):
    with pytest.raises(Exception) as exc:
        bonus_calculation(er[0], er[1])
    assert str(exc.value) == er[2], "Exception text is incorrect!"

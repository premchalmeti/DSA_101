companies = dict()


def register_company(company_dict):
    import datetime
    """
        :company: dict(id, name)
    """
    company_dict['emps'] = dict()
    company_dict['registeration_date'] = str(datetime.datetime.now())

    companies[company_dict['id']] = company_dict

    return company_dict


def _check_is_registered(company, emp=None):
    if company['id'] not in companies:
        raise Exception("Company is not registered")

    if emp and emp['id'] not in company['id']['emps']:
        raise Exception("Employee is not recruited")

    return True


def add_new_emp(emp, company):
    _check_is_registered(company)
    emp['on_role'] = False
    company['emps'][emp['id']] = emp
    return emp


def put_emp_on_role(company, emp):
    _check_is_registered(company, emp)
    company['emps'][emp['id']]['on_role'] = True


def filter_emps(company, on_role=True):
    _check_is_registered(company)

    return filter(
        lambda emp: emp['on_role'] == on_role,
        company['emps'].values()
    )


def sort_company(by='id', desc_order=False):
    comps = companies.values()
    comps.sort(
        key=lambda company: company[by], reverse=desc_order
    )
    return comps


def sort_emp(company, by='id', desc_order=False):
    emps = company['emps'].values()
    emps.sort(
        key=lambda emp: emp[by], reverse=desc_order
    )
    return emps


if __name__ == '__main__':
    incentius = register_company(dict(id=123, name='Incentius'))

    premkumar = add_new_emp(
        company=incentius, emp=dict(
            id=123, name='Premkumar Ashok Chalmeti', dob='30/05/1996'
        )
    )

    kartik = add_new_emp(
        company=incentius, emp=dict(
            id=321, name='Kartik Puri', dob='01/10/1995'
        )
    )

    print(filter_emps(company=incentius, on_role=False))

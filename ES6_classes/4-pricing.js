import Currency from './3-currency';

export default class Pricing {
  constructor(amount = 0, currency = '') {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(value) {
    this._amount = value;
  }

  set currency(value) {
    this._currency = value;
  }

  get amount() {
    return this._amount;
  }

  get currency() {
    return this._currency;
  }
}

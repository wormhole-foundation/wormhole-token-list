test("markets.json is valid", () => {
  const Ajv = require("ajv");
  const ajv = new Ajv(); // options can be passed, e.g. {allErrors: true}

  const schema = require("../markets.schema.json");

  const validate = ajv.compile(schema);

  const data = require("../markets.json");

  const valid = validate(data);

  expect(valid).toBe(true);
});
test("all markets are keys in markets", () => {
  const data = require("../markets.json");
  for (const sourceChain in data.marketsBySource) {
    for (const targetChain in data.marketsBySource[sourceChain]) {
      for (const address in data.marketsBySource[sourceChain][targetChain]) {
        data.marketsBySource[sourceChain][targetChain][address].markets.forEach(
          (market) => {
            expect(data.markets[market]).toBeDefined();
          }
        );
      }
    }
  }
});

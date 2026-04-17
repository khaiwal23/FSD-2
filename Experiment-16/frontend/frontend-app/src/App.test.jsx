import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import "@testing-library/jest-dom/vitest";
import App from "./App";

test("button render ho raha hai", () => {
  render(<App />);
  const btn = screen.getByText("Submit");
  expect(btn).toBeInTheDocument();
});
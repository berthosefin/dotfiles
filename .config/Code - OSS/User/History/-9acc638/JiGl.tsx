import React from "react";

export default function AboutLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <nav>About Navbar</nav>
      <main>{children}</main>
    </>
  );
}

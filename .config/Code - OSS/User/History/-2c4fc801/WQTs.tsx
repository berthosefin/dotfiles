"use client";

import Container from "./Container";

const Navbar = () => {
  return (
    <div className="fixed w-full bg-white z-10 shadow-sm">
      <div className="py-4 border-b-[1px]">
        <Container>
          <div className="flex flex-ro"></div>
        </Container>
      </div>
    </div>
  );
};

export default Navbar;

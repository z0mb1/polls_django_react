import React from "react";
import classNames from "classnames";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import Button from "@material-ui/core/Button";

const NavBar = props => {
  return (
    <AppBar
      position="fixed"
      className={classNames(props.classes.appBar, {
        [props.classes.appBarShift]: props.isOpen
      })}
    >
      <Toolbar disableGutters={!props.isOpen}>
        <IconButton
          color="inherit"
          aria-label="Open drawer"
          onClick={props.handleDrawerOpen}
          className={classNames(props.classes.menuButton, {
            [props.classes.hide]: props.isOpen
          })}
        >
          <MenuIcon />
        </IconButton>
        <Typography variant="h6" color="inherit" noWrap>
          {props.title}
        </Typography>
        <Button color="inherit">Войти</Button>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;

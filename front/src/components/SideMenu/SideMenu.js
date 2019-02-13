import React from "react";
import classNames from "classnames";
import Drawer from "@material-ui/core/Drawer";
import List from "@material-ui/core/List";
import Divider from "@material-ui/core/Divider";
import IconButton from "@material-ui/core/IconButton";
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft";
import ChevronRightIcon from "@material-ui/icons/ChevronRight";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import InboxIcon from "@material-ui/icons/MoveToInbox";
import MailIcon from "@material-ui/icons/Mail";
import QueestionIcon from "@material-ui/icons/QuestionAnswer";

const sidebarFill = [
  { name: "Ответить", icon: <QueestionIcon /> },
  { name: "Создать", icon: <InboxIcon /> },
  { name: "Результаты", icon: <MailIcon /> }
];

const SideMenu = props => {
  return (
    <Drawer
      variant="permanent"
      className={classNames(props.classes.drawer, {
        [props.classes.drawerOpen]: props.isOpen,
        [props.classes.drawerClose]: !props.isOpen
      })}
      classes={{
        paper: classNames({
          [props.classes.drawerOpen]: props.isOpen,
          [props.classes.drawerClose]: !props.isOpen
        })
      }}
      open={props.isOpen}
    >
      <div className={props.classes.toolbar}>
        <IconButton onClick={props.handleDrawerClose}>
          {props.theme.direction === "rtl" ? (
            <ChevronRightIcon />
          ) : (
            <ChevronLeftIcon />
          )}
        </IconButton>
      </div>
      <Divider />
      <List>
        {sidebarFill.map(({ name, icon }) => (
          <ListItem button key={name}>
            <ListItemIcon>{icon}</ListItemIcon>
            <ListItemText primary={name} />
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
};

export default SideMenu;

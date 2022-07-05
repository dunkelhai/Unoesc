using System;
using System.Collections.Generic;
using System.Text;

namespace UNO.BL
{
    public class OrderItem
    {
        public OrderItem()
        {
        }

        public OrderItem(int orderItemId)
        {
            OrderItemId = orderItemId;
        }

        public int OrderItemId { get; private set; }

        public int ProductId { get; set; }
        public Product Product { get; }

        public int OrderId { get; set; }
        public Order Order { get; set; }

        public decimal? PurchasePrice { get; set; }
        public int Quantity { get; set; }

        public bool Validate()
        {
            var isValid = true;

            if(Quantity <= 0)
            {
                isValid = false;
            }
            if(ProductId <= 0)
            {
                isValid = false;
            }
            if(PurchasePrice == null)
            {
                isValid = false;
            }

            return isValid;

        }


    }
}
